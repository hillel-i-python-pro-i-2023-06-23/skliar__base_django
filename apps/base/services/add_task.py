from apps.base.models import ToDoList


def add_task(name_task, check):
    new_task = ToDoList.objects.create(
        task=name_task,
        is_done=check,
    )
    return new_task
