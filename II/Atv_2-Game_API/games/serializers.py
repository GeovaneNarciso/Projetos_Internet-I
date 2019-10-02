from rest_framework import serializers
from games.models import Game
from datetime import datetime


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')

    def validate_name(self, data):
        game = Game.objects.filter(name=data)
        if game:
            msg = "Jogos não podem ter nomes iguais."
            raise serializers.ValidationError(msg)
        return data

    def validate_delete(self, game):
        if game.release_date >= datetime.now():
            return True
        else:
            msg = "Jogos já lançados não podem ser deletados."
            raise serializers.ValidationError(msg)
