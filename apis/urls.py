from django.urls import path
from .views import CreateShortURL, ShortURLDetail, GetURLStatistics

urlpatterns = [
    path('', CreateShortURL.as_view(), name='create_short_url'),
    path('shorten/', CreateShortURL.as_view(), name='create_short_url'),
    path('<str:short_code>/', ShortURLDetail.as_view(), name='short_url_detail'),
    path('<str:short_code>/stats/', GetURLStatistics.as_view(), name='url_statistics'),
]
