from django.db import models
from django.conf import settings


# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=300, null=False)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.user.username