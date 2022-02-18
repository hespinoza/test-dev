from rest_framework import serializers

from adventure import models


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()
    
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'

class ServiceAreaSerializer(serializers.Serializer):
    kilometer = serializers.IntegerField()
    gas_price = serializers.IntegerField()
