from django.db import models


class ContactType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип данных")

    def __str__(self):
        return self.name


class ContactData(models.Model):
    contact_type = models.ForeignKey("ContactType", on_delete=models.CASCADE, verbose_name="Тип данных")
    value = models.CharField(max_length=255)  # Здесь можно добавить валидацию по типу контакта
    contact = models.ForeignKey(
        "Contact",
        related_name="contact_data",
        on_delete=models.CASCADE,
        verbose_name="Контактные данные",
    )  # Связь с Contact моделью

    def __str__(self):
        return self.value


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    birthdate = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    groups = models.ManyToManyField("Group", verbose_name="Группы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
