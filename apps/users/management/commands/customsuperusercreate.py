import getpass
from django.core.management.base import BaseCommand
from apps.users.models import User


class Command(BaseCommand):
    help = "Create a superuser"

    def handle(self, *args, **options):
        print("new superuser - 1\ndefault user 2")
        choice = input("your choice")

        if choice == "1":
            username = input("Enter the desired username: ")
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.ERROR(f"User {username} already exists"))

            password = getpass.getpass("Enter the password: ")
            password_confirm = getpass.getpass("Confirm the password: ")

            if password != password_confirm:
                self.stderr.write(self.style.ERROR("Passwords do not match"))
                return

            try:
                user = User.objects.create_superuser(
                    username=username,
                    password=password,
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Superuser '{username}' created successfully"),
                )
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error creating superuser: {e}"))
        elif choice == "2":
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
