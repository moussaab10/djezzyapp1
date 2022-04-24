from django.apps import AppConfig


class GreenevConfig(AppConfig):
    name = 'greenev'
    def ready(self):
        import greenev.signals