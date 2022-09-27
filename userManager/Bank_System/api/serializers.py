from rest_framework import serializers
from Bank_System.models import Bank, Taka

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"
        
class TakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taka
        fields = "__all__"