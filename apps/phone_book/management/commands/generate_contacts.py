from django.core.management.base import BaseCommand
from apps.phone_book.services.generate_data import generate_phones
from apps.phone_book.models import Contact


class Command(BaseCommand):
    help = "Generate fake data for your models"

    def handle(self, *args, **kwargs):
        try:
            if not Contact.objects.exists():
                generate_phones()
                self.stdout.write(
                    self.style.SUCCESS("table is full"),
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS("table is not empty"),
                )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error generate data: {e}"))
