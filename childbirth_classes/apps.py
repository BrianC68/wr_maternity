from django.apps import AppConfig


class ChildbirthClassesConfig(AppConfig):
    name = 'childbirth_classes'
    verbose_name = 'Childbirth Classes'

    def ready(self):
        import wr_maternity.signals.hooks
