from django.apps import AppConfig


class IscopeRecreateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ISCOPE_Recreate'

    def ready(self):
        import ISCOPE_Recreate.signals