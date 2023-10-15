from django.apps import AppConfig

from analysis.ml_models import initialize_models


class AnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analysis'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import analysis.signals

        initialize_models()
