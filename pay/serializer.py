from rest_framework import fields
from rest_framework import serializers
from .models import Transaction, Cards
from .constants import currency_list, payment_method
from datetime import date

class card_check(serializers.Serializer):
    number= fields.IntegerField(required=True)
    expirationMonth= fields.IntegerField(required=True)
    expirationYear = fields.IntegerField(required=True)
    cvv = fields.IntegerField(required=True)

    def validate_number(self, value):
        if len(str(value)) == 16:
            return value
        raise serializers.ValidationError("Card Number should be of 16 digits")
    
    def validate_expirationMonth(self,value):
        if int(value) in range(1,13):
            return value
        raise serializers.ValidationError("expiry month should be in range of 1 to 12")

    def validate_year(self,value):
        if len(str(value)) == 4:
            return value
        raise serializers.ValidationError("Card Number should be of 4 digits")

    def validate_cvv(self,value):
        if len(str(value)) == 3:
            return value
        raise serializers.ValidationError("Card Number should be of 3 digits")

class payment_check(serializers.Serializer):
    amount = fields.IntegerField(required=True)
    currency = fields.CharField(required=True)
    paytype = fields.CharField(required=True)
    card = card_check()


    def validate_currency(self, value):
        if value in currency_list:
            return value
        raise serializers.ValidationError(" The Value Should Specific Currency")

    def validate_paytype(self, value):
        if value in payment_method:
            return value
        raise serializers.ValidationError(" please specific payment method")
    
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = [
            "number"
        ]

class ReadTransaction(serializers.ModelSerializer):
    number = CardSerializer()
    class Meta:
    
        model = Transaction
        fields = [
            "amount",
            "currency",
            "paytype",
            "number",
            "status",
            "create_datetime",
            "authorization_code"
        ]
        



