from django.shortcuts import redirect, render
from django.core.management import call_command

# Create your views here.


def home_page(request):
    return render(request, "phone_book/home_page.html")


def generate_fake_data(request):
    call_command("populate_data")
    return redirect("base")
