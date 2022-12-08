from django.apps import AppConfig


class StudiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studies'

    def ready(self, *args, **kwargs) -> None:
        import studies.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready
