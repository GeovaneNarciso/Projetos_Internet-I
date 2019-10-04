from rest_framework import serializers
from games.models import Game
from datetime import datetime


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    @staticmethod
    def validate_name(data):
        game = Game.objects.filter(name=data)
        if game:
            msg = "Jogos não podem ter nomes iguais."
            raise serializers.ValidationError(msg)
        return data

    @staticmethod
    def validate_delete(game):
        if game.release_date >= datetime.now():
            return True
        else:
            msg = "Jogos já lançados não podem ser deletados."
            raise serializers.ValidationError(msg)
