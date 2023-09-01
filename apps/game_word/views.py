from django.shortcuts import render
from .models import Word, GameRoom, Player, PlayerGameRoom

# Create your views here.


def base_game(request):
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
            max_players=4,  # You can adjust this as needed
        )

        # Create Player instances and add them to the GameRoom
        for player_name in player_names:
            player, created = Player.objects.get_or_create(name=player_name)
            PlayerGameRoom.objects.get_or_create(player=player, game_room=game_room)

        return render(request, template_name="game_word/room_page.html", context={"title": "Game"})

    return render(request, template_name="game_word/game_home.html", context={"title": "Game"})


def room_page(request):
    game_room_id = 1
    room = GameRoom.objects.get(id=game_room_id)
    room_name = "no"
    if room:
        room_name = room.name
    if request.method == "POST":
        pass
    return render(
        request,
        template_name="game_word/room_page.html",
        context={"title": "Game", "room_name": room_name},
    )
