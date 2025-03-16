from django.urls import path
from .views import CreateShortURL, redirect_to_original

urlpatterns = [
    path('shorten/', CreateShortURL.as_view(), name='create-short-url'),
    path('<str:short_code>/', redirect_to_original, name='redirect-to-original'),
]
