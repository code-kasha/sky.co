from django.db import models

from .managers import SKYUrlManager

class SKYUrl(models.Model):
    url = models.CharField(max_length=250)
    short_code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = SKYUrlManager()

    class Meta:
        verbose_name = "SKYUrl"
        verbose_name_plural = "SKYUrls"

    def __str__(self):
        return self.url
