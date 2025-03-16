from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortURL
from .serializers import ShortURLSerializer

class CreateShortURL(APIView):

    def get(self, request):
        # Render the HTML template for the frontend
        return render(request, 'create_short_url.html')
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def redirect_to_original(request, short_code):
    print('Short Code recieved',short_code)
    url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(url.original_url)

class RetrieveOriginalURL(APIView):
    def get(self, request, short_code):
        # Retrieve the ShortURL object or return 404
        url = get_object_or_404(ShortURL, short_code=short_code)

        # Increment the access count
        url.access_count += 1
        url.save()

        # Return JSON data for API requests
        if request.accepted_renderer.format == 'json':
            return Response(ShortURLSerializer(url).data)

        # Render the template with the URL details
        return render(request, 'retrieve_url.html', {'url': url})

class UpdateShortURL(APIView):
    def put(self, request, short_code):
        url = get_object_or_404(ShortURL, short_code=short_code)

        if 'url' not in request.data:
            return Response(
                {"error": "The 'url' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        url.original_url = request.data['url']
        url.save()

        serializer = ShortURLSerializer(url)
        return Response(serializer.data, status=status.HTTP_200_OK)
