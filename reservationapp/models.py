from django.db import models


# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=25)
    operatingAirline = models.CharField(max_length=25)
    departureCity = models.CharField(max_length=25)
    arrivalCity = models.CharField(max_length=25)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()


class Passenger(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
