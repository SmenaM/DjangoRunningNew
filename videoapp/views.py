from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  
from django.conf import settings
from videoapp.video_creator import generate_video 
from videoapp.models import VideoRequest
import os

@csrf_exempt  
def create_video_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        color_choice = request.POST.get('color')
        background_choice = request.POST.get('background')

        # Сохранение запроса в базу данных
        VideoRequest.objects.create(
            message=message,
            color_choice=color_choice,
            background_choice=background_choice
        )

        video_path = generate_video(message, color_choice, background_choice)  
        if video_path:
            video_url = settings.MEDIA_URL + os.path.basename(video_path)
            return redirect(video_url) 
        else:
            return HttpResponse("Ошибка создания видео")
    else:
        return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')