from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Upload(models.Model):
    operation = models.ForeignKey('operations.Operation', on_delete=models.CASCADE, related_name='uploads')
    image = models.ImageField(upload_to='operations_image/%Y/%m/%d/', help_text='Upload operation images')
    caption = models.CharField(max_length=255, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.operation.task.title}"
    
    class Meta:
        ordering = ['-uploaded_at']