from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from decouple import config

DJANGO_SUPEUSER_USERNAME = config('DJANGO_SUPEUSER_USERNAME')
DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPEUSER_PASSWORD')
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL')

User = get_user_model()

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        try:
            user = User(
                email=DJANGO_SUPERUSER_EMAIL,
                username=DJANGO_SUPERUSER_USERNAME
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_superuser = True
            user.is_admin = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created well.'))
        except Exception as e:
            raise CommandError(e)