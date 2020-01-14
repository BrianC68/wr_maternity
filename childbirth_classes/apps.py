from django.apps import AppConfig


class ChildbirthClassesConfig(AppConfig):
    '''Configuration for childbirth_classes app.'''
    name = 'childbirth_classes'
    verbose_name = 'Childbirth Classes'

    # Register signals for PayPal IPN app
    def ready(self):
        import wr_maternity.signals.hooks
