from django.apps import AppConfig


class DoulaTrainingConfig(AppConfig):
    name = 'doula_training'
    verbose_name = 'Doula Training'

    def ready(self):
        import wr_maternity.signals.hooks
