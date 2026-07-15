from django.db import models
from django.contrib.auth.models import User


class QRCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()
    image = models.ImageField(upload_to="qr_codes/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.data[:30]}"