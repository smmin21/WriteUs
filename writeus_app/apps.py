from django.apps import AppConfig
from .gpt.kogpt2 import kogpt2


class WriteusAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "writeus_app"
    generator = kogpt2()