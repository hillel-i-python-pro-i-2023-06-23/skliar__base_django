from django.shortcuts import render
from apps.phone_book.models import Contact


# Create your views here.


def home_page(request):
    contacts = Contact.objects.all()
    return render(request, "phone_book/home_page.html", context={"contacts": contacts})
