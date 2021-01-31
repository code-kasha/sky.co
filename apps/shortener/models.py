from django.db import models


class SKYUrl(models.Model):
    url = models.CharField(max_length=250)

    def __str__(self):
        return self.url
