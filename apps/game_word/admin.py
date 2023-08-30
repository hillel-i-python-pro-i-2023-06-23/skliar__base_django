from django.contrib import admin
from .models import Word, GameRoom, Player, PlayerGameRoom

# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(GameRoom)
class GameRoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "current_state",
    )


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "guessed_letters",
    )


@admin.register(PlayerGameRoom)
class PlayerGameRoomAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "joined_at",
    )
