# import getpass
from django.core.management.base import BaseCommand
from apps.users.models import User


class Command(BaseCommand):
    help = "Create an admin"

    def handle(self, *args, **options):
        try:
            if User.objects.filter(username="admin").exists():
                self.stdout.write(
                    self.style.WARNING("Superuser 'admin' already exists"),
                )
            else:
                user = User.objects.create_superuser(
                    username="admin",
                    password="admin123",
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Superuser {user} created successfully"),
                )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error creating superuser: {e}"))
