from django.shortcuts import render
from .models import Word, GameRoom, Player, PlayerGameRoom

# Create your views here.


def all_room(request):
    rooms = GameRoom.objects.all()
    return render(request, template_name="game_word/all_rooms.html", context={"title": "All rooms", "rooms": rooms})


def add_room_and_start(request):
    if request.method == "POST":
        # Get data from the form
        players_input = request.POST.get("name_players")
        input_word = request.POST.get("input_word")
        room_name = request.POST.get("name_room")

        # Split the player names input into a list
        player_names = [name.strip() for name in players_input.split()]

        # Create Word instance
        word, created = Word.objects.get_or_create(name=input_word)

        # Create GameRoom instance
        game_room, created = GameRoom.objects.get_or_create(
            name=room_name,
            word_to_guess=word,
            current_state="_" * len(input_word),
        )

        # Create Player instances and add them to the GameRoom
        for player_name in player_names:
            player, created = Player.objects.get_or_create(name=player_name)
            PlayerGameRoom.objects.get_or_create(player=player, game_room=game_room)

        return render(request, "game_word/room_page.html")

    return render(request, template_name="game_word/add_game.html", context={"title": "Game"})
