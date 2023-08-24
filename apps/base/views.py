from django.shortcuts import render, redirect
from apps.base.services.add_task import add_task
from .models import ToDoList

# Create your views here.


def home_page(request):
    if request.method == "POST":
        task = request.POST.get("name_task")
        check = request.POST.get("check")

        is_done = check == "true" if check is not None else False
        try:
            add_task(name_task=task, check=is_done)
            return redirect("base:home_page")
        except Exception:
            return render(request, template_name="base/home_page.html", context={"title": "Home page"})

    tasks = ToDoList.objects.all()

    return render(request, template_name="base/home_page.html", context={"title": "Home page", "tasks": tasks})
