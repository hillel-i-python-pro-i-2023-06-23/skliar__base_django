from django.contrib import admin
from .models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "is_done",
    )

    list_filter = ("is_done",)
