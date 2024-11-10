import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "sample_django_app.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import sample_django_app.users.signals  # noqa: F401
