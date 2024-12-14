from rest_framework import serializers
from .models import Flight, Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight']  # Ensure 'flight' is included

class FlightSerializer(serializers.ModelSerializer):
    passengers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Include related passengers

    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'departure', 'arrival', 'origin', 'destination', 'capacity', 'passengers']
