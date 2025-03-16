from django.shortcuts import render, get_object_or_404, redirect
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
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ShortURLDetail(APIView):
    def get_object(self, short_code):
        return get_object_or_404(ShortURL, short_code=short_code)

    def get(self, request, short_code):
        url = self.get_object(short_code)
        url.access_count += 1
        url.save()
        return Response(ShortURLSerializer(url).data)

    def put(self, request, short_code):
        url = self.get_object(short_code)
        if 'url' not in request.data:
            return Response(
                {"error": "The 'url' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        url.original_url = request.data['url']
        url.save()
        return Response(ShortURLSerializer(url).data, status=status.HTTP_200_OK)

    def delete(self, request, short_code):
        url = self.get_object(short_code)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GetURLStatistics(APIView):
    def get(self, request, short_code):
        # Retrieve the ShortURL object or return 404
        url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(url)
        return Response(serializer.data, status=status.HTTP_200_OK)

