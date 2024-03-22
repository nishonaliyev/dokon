# serializers.py
from rest_framework import serializers
from .models import Mahsulot, Buyurtma, BuyurtmaMahsulot, Chegirma

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'

class ChegirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chegirma
        fields = '__all__'

class BuyurtmaMahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyurtmaMahsulot
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    mahsulotlar = MahsulotSerializer(many=True, read_only=True)
    chegirmalar = ChegirmaSerializer(many=True, read_only=True)

    class Meta:
        model = Buyurtma
        fields = '__all__'
