
from rest_framework import serializers, fields
from codetest.currency.models import Convert, Currency


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = ['name', 'rate']


class ConvertSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(many=True)
    class Meta:
        model = Convert
        fields = ['id', 'base_currency', 'date', 'currency']

