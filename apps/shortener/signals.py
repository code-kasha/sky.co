from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import SKYUrl

from apps.utils.helpers import generate_short_code


@receiver(pre_save, sender=SKYUrl)
def pre_save_add_short_code(sender, instance, *args, **kwargs):
    if not instance.short_code:
        code = generate_short_code(instance)
        instance.short_code = code