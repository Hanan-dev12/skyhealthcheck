from django.apps import AppConfig


from django.contrib.auth import get_user_model
from django.db.utils import OperationalError

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        try:
            User = get_user_model()
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser('Hanan', 'admin@gmail.com', 'admin')
                print("✅ Default superuser created: Hanan / admin")
        except OperationalError:
            # Ignore during initial migration or db setup
            pass
