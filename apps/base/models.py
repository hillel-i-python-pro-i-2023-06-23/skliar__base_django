from django.db import models

# Create your models here.


class ToDoList(models.Model):
    task = models.CharField(max_length=150)
    is_done = models.BooleanField(default=False)

    # def __str__(self):
    #     return (
    #         f"task {self.task}  check {self.is_done}"
    #     )

    # class Meta:
    #     ordering = ['is_done']
