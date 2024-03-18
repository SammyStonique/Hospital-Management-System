from django.apps import AppConfig


class FinancialAccountsChartOfAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'financial_accounts_chart_of_accounts'

    def ready(self):
        import financial_accounts_chart_of_accounts.signals