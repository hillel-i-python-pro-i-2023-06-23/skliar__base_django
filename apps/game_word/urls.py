from django.urls import path
from . import views

app_name = "game_word"

urlpatterns = [
    path("add_room", views.add_room_and_start, name="add_room"),
    path("all_rooms", views.all_room, name="all_rooms"),
]
