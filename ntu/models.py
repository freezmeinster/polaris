from django.db import models

class PublicKey(models.Model):

    user = models.CharField(max_length=255)
    key = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user
