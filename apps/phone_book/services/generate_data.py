from apps.phone_book.models import Contact, ContactType, Group, ContactData
from faker import Faker


def generate_phones():
    fake = Faker()
    contact_types = ["Email", "Phone", "Address"]  # Замените на ваши типы контактов

    # Генерация данных для модели ContactType
    for type_name in contact_types:
        ContactType.objects.get_or_create(name=type_name)

    # Генерация данных для модели Group
    for _ in range(10):  # Создадим 10 групп
        Group.objects.get_or_create(name=fake.word())

    # Генерация данных для модели Contact и ContactData
    for _ in range(10):  # Создадим 100 контактов
        contact = Contact.objects.create(
            name=fake.name(),
            birthdate=fake.date_of_birth(minimum_age=18, maximum_age=80, tzinfo=None),
        )
        contact.groups.add(*Group.objects.order_by("?")[:3])  # Добавляем 3 случайные группы

        for _ in range(3):  # Создадим 3 случайных контактных данных для каждого контакта
            contact_data_type = ContactType.objects.get(name=fake.random_element(contact_types))
            contact_data = ContactData.objects.create(contact_type=contact_data_type, value=fake.email())
            contact.contact_data.add(contact_data)  # Связываем контакт с контактными данными
