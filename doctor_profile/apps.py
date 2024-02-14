from django.apps import AppConfig


class DoctorProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctor_profile'

    def ready(self):
        import doctor_profile.signals
