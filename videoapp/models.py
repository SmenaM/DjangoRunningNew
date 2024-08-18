from django.db import models

class VideoRequest(models.Model):
    message = models.CharField(max_length=255)
    color_choice = models.CharField(max_length=1)
    background_choice = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.message} ({self.color_choice}, {self.background_choice})"