from django.db import models

# Create your models here.


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class GameRoom(models.Model):
    id = models.AutoField(primary_key=True)  # Уникальный идентификатор записи
    name = models.CharField(max_length=100, unique=True)  # Название игровой комнаты
    word_to_guess = models.ForeignKey(Word, on_delete=models.CASCADE)  # Ссылка на слово для угадывания
    current_state = models.CharField(max_length=100)  # Текущее состояние слова с открытыми буквами
    players = models.ManyToManyField("Player", through="PlayerGameRoom")  # Связь с игроками через PlayerGameRoom

    def __str__(self):
        return self.name


class Player(models.Model):
    id = models.AutoField(primary_key=True)  # Уникальный идентификатор записи
    name = models.CharField(max_length=100)  # Имя игрока
    guessed_letters = models.CharField(max_length=26, default="")  # Угаданные буквы игрока

    def __str__(self):
        return self.name


class PlayerGameRoom(models.Model):
    id = models.AutoField(primary_key=True)  # Уникальный идентификатор записи
    player = models.ForeignKey(Player, on_delete=models.CASCADE)  # Ссылка на игрока
    game_room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)  # Ссылка на игровую комнату
    joined_at = models.DateTimeField(auto_now_add=True)  # Дата и время присоединения игрока к комнате

    def __str__(self):
        return f"{self.player.name} - {self.game_room.name}"
