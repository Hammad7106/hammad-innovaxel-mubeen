from django.urls import path
from .views import CreateShortURL, ShortURLDetail, GetURLStatistics

urlpatterns = [
    path('', CreateShortURL.as_view(), name='create_short_url'),

    # Create Short Url
    path('shorten/', CreateShortURL.as_view(), name='create_short_url'),

    # Retrieve, Update and Delete the Url
    path('<str:short_code>/', ShortURLDetail.as_view(), name='short_url_detail'),

    # Check the Stats of Url Clicked
    path('<str:short_code>/stats/', GetURLStatistics.as_view(), name='url_statistics'),
]
