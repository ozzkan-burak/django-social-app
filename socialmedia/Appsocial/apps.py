from django.apps import AppConfig


class AppsocialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Appsocial"

    def ready(self):
        import Appsocial.signals