from django.apps import AppConfig


class DoulaTrainingConfig(AppConfig):
    '''Configuration for doula_training app.'''
    name = 'doula_training'
    verbose_name = 'Doula Training'

    # Register signals for PayPal IPN app
    def ready(self):
        import wr_maternity.signals.hooks
