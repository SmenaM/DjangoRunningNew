from django.contrib import admin
from .models import VideoRequest

@admin.register(VideoRequest)
class VideoRequestAdmin(admin.ModelAdmin):
    list_display = ('message', 'color_choice', 'background_choice', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('message', 'color_choice', 'background_choice')