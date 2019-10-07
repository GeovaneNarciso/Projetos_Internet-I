from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'owner', 'balance', 'creation_date')

    @staticmethod
    def validate_balance(data):
        if data < 0:
            msg = "Saldo não pode ser negativo."
            raise serializers.ValidationError(msg)
        return data

    """@staticmethod
    def validate_creation_data(data):
        if data["creation_date"]:
            msg = "Não é permitido informar uma data."
            raise serializers.ValidationError(msg)
        return data"""
