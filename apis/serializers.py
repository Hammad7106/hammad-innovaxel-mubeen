from rest_framework import serializers
from .models import ShortURL

class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'short_code', 'created_at', 'updated_at', 'access_count']
