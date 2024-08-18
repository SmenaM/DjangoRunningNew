import cv2
import numpy as np
import os
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw, ImageFont

# Параметры видео
width = 100  # Ширина кадра
height = 100  # Высота кадра
fps = 24  # Количество кадров в секунду
duration = 3  # Продолжительность видео в секундах

def generate_video(message, color_choice, background_choice):
    # Выбор цвета текста
    color_dict = {
        'R': (0, 0, 255),  # Красный
        'G': (0, 255, 0),  # Зеленый
        'B': (255, 0, 0),  # Синий
        'Y': (0, 255, 255),  # Желтый
        'M': (255, 0, 255),  # Пурпурный
        'C': (255, 255, 0),  # Голубой
        'W': (255, 255, 255),  # Белый
        'K': (0, 0, 0)   # Черный
    }

    font_color = color_dict.get(color_choice.upper(), (255, 255, 255))
    background_color = color_dict.get(background_choice.upper(), (0, 0, 0))

    try:
        # Создание видеопотока и формирование пути к видео в папке media
        if not hasattr(settings, 'MEDIA_ROOT'):
            print("Ошибка: settings.MEDIA_ROOT не определен")
            return None

        # Создаем директорию media, если она не существует
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        video_filename = f'output_{timestamp}.avi'
        video_path = os.path.join(settings.MEDIA_ROOT, video_filename)

        # Создание видеопотока
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

        # Путь к шрифту
        font_path = "DroidSerif-Regular.ttf"  
        font_size = 20  # Размер шрифта
        font = ImageFont.truetype(font_path, font_size)

        # Начальные координаты текста
        x = width
        y = height // 2 - 10  # Сдвиг по вертикали для корректного отображения текста

        # Создание кадров видео
        for i in range(int(duration * fps)):
            # Создание пустого кадра с фоном
            frame = np.full((height, width, 3), background_color, dtype=np.uint8)

            # Конвертация кадра в изображение PIL
            pil_image = Image.fromarray(frame)
            draw = ImageDraw.Draw(pil_image)

            # Добавление текста на кадр
            draw.text((x, y), message, font=font, fill=font_color)

            # Конвертация обратно в формат OpenCV
            frame = np.array(pil_image)

            # Перемещение текста
            x -= 2  # Скорость бегущей строки
            if x < -len(message) * font_size // 2:  # Если текст полностью ушел за экран
                x = width  # Переместите его обратно к правому краю

            # Запись кадра в видео
            out.write(frame)

        # Закрытие видеопотока
        out.release()

        # Возвращаем полный путь к видеофайлу
        return video_path

    except Exception as e:
        print(f"Ошибка при создании видео: {e}")
        return None