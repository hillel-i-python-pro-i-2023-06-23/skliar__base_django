from django.urls import path
from . import views

app_name = "phone_book"

urlpatterns = [
    path("home/", views.home_page, name="home_page"),
    path("generate_user/", views.generate_users, name="generate_user"),
]
