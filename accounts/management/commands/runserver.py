from django.core.management.commands.runserver import Command as OriginalRunserver
from django.contrib.auth import get_user_model

class Command(OriginalRunserver):
    def handle(self, *args, **options):
        self.create_default_superuser()
        super().handle(*args, **options)

    def create_default_superuser(self):
        User = get_user_model()
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin12345'

        if not User.objects.filter(username=username).exists():
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'✅ Auto superuser created: {username}/{password}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Failed to create superuser: {e}'))
        else:
            self.stdout.write(self.style.WARNING(f'⚠️ Superuser "{username}" already exists.'))
