from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "iron_man.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import iron_man.users.signals  # noqa F401
        except ImportError:
            pass
