from django.urls import path
from .views import CreateShortURL, redirect_to_original, RetrieveOriginalURL, UpdateShortURL

urlpatterns = [
    path('shorten/', CreateShortURL.as_view(), name='create-short-url'),
    # path('<str:short_code>/', redirect_to_original, name='redirect-to-original'),
    path('<str:short_code>/', RetrieveOriginalURL.as_view(), name='retrieve-original-url'),
    path('update/<str:short_code>/', UpdateShortURL.as_view(), name='update-short-url'),
]
