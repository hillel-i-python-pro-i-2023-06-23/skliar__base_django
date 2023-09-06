from django.shortcuts import render, redirect
from apps.phone_book.models import Contact
from apps.phone_book.services.generate_data import generate_phones


# Create your views here.


def home_page(request):
    contacts = Contact.objects.all()
    return render(request, "phone_book/home_page.html", context={"contacts": contacts, "title": "Contacts"})


def generate_users(request):
    if request.method == "POST":
        generate_phones()

        return redirect("phone_book:home_page")

    return render(request, "phone_book/home_page.html")
