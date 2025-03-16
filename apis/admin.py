
from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at', 'updated_at', 'access_count')
    search_fields = ('url', 'short_code')
    list_filter = ('created_at', 'updated_at')
