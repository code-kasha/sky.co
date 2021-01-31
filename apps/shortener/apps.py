from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    name = 'apps.shortener'

    def ready(self):
        import apps.shortener.signals
        