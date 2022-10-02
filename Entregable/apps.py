from django.apps import AppConfig


class EntregableConfig(AppConfig):
    name = 'Entregable'

    def ready(self):
        import Entregable.signals

