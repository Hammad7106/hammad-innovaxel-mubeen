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
