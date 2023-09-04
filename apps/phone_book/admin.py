from django.contrib import admin
from .models import ContactType, ContactData, Group, Contact


@admin.register(ContactType)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ("contact_type", "value")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "display_groups", "display_contact_data")

    def display_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    def display_contact_data(self, obj):
        return ", ".join([data.value for data in obj.contact_data.all()])
