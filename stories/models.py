from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="stories/images/",
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Story ({self.created_at})"
