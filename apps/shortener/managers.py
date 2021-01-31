from django.db import models

class SKYUrlManager(models.Manager):
    def active(self):
        qs = self.get_queryset().filter(is_active=True)
        return qs

    def inactive(self):
        qs = self.get_queryset().filter(is_active=False).distinct()
        return qs

    def refresh_shortcodes(self):
        qs = self.get_queryset()
        new_codes = 0
        for q in qs:
            q.short_code = None
            q.save()
            new_codes += 1
        return new_codes

    def refresh_shortcode(self, id):
        obj = self.get_queryset().filter(id=id).first()
        obj.short_code = None
        obj.save()
        return obj
        

