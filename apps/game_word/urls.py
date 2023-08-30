from django.urls import path
from . import views

app_name = "game_word"

urlpatterns = [
    path("home", views.base_game, name="game_home"),
]
