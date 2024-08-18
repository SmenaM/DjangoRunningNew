from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from videoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create_video/', views.create_video_view, name='create_video'),
]

# Подключение медиа-файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)