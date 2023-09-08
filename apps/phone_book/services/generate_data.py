from django.db import transaction
from apps.phone_book.models import Contact, ContactType, Group, ContactData
from faker import Faker
import random

fake = Faker()


def generate_phones():
    # Определите модели ContactType, Group, Contact и ContactData здесь

    # Ваши типы контактов
    contact_types = ["Email", "Phone", "Address"]

    # Генерация данных для модели ContactType
    for type_name in contact_types:
        ContactType.objects.get_or_create(name=type_name)

    # Генерация данных для модели Group
    for _ in range(10):
        Group.objects.get_or_create(name=fake.word())

    # Генерация данных для моделей Contact и ContactData
    with transaction.atomic():
        for _ in range(10):
            contact = Contact.objects.create(
                name=fake.name(),
                birthdate=fake.date_of_birth(minimum_age=18, maximum_age=80),
            )
            contact.groups.add(*random.sample(list(Group.objects.all()), 3))

            for _ in range(3):
                contact_data_type = ContactType.objects.get(name=random.choice(contact_types))
                if contact_data_type.name == "Phone":
                    contact_data_value = fake.phone_number()
                elif contact_data_type.name == "Address":
                    contact_data_value = fake.address()
                else:
                    contact_data_value = fake.email()

                # Создание ContactData и связь с Contact
                contact_data = ContactData.objects.create(  # noqa
                    contact=contact,
                    contact_type=contact_data_type,
                    value=contact_data_value,
                )
