from django.apps import AppConfig


class PatientsRegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients_registration'

    def ready(self):
        import financial_accounts_chart_of_accounts.signals