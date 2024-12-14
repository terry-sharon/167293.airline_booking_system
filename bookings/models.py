from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=50, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} ({self.origin} -> {self.destination})"

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(
        Flight,
        related_name='passengers',  # Allows reverse lookup from Flight to Passenger
        on_delete=models.CASCADE  # Deletes passengers when the flight is deleted
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
