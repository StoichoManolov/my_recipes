from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'My_Recipes.accounts'

    def ready(self):
        import My_Recipes.accounts.signals
