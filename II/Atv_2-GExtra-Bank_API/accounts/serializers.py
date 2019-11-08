from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'owner', 'balance', 'creation_date')

    def create(self, validated_data):
        if validated_data["balance"] < 0:
            msg = {"message": "Não é permitido saldo negativo."}
            raise serializers.ValidationError(msg)
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "owner" in validated_data:
            msg = {"message": "Apenas o saldo pode ser atualizado."}
            raise serializers.ValidationError(msg)
        if validated_data["balance"] == 0:
            msg = {"message": "Valor não pode ser zero."}
            raise serializers.ValidationError(msg)
        elif validated_data["balance"] > 0:
            instance.balance += validated_data["balance"]
            instance.save()
        elif validated_data["balance"] < 0:
            instance.balance += validated_data["balance"]
            if instance.balance < 0:
                msg = {"message": "Saldo insuficiente."}
                raise serializers.ValidationError(msg)
            else:
                instance.save()
        return instance
