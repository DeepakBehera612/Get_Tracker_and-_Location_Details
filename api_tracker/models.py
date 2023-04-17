from django.db import models
import psycopg2

# Create your models here.

con = psycopg2.connect(user="postgres", password="admin",
                       host="localhost", port="5432", database="db_tracker_location")


class Tracker_Models(models.Model):
    imei = models.CharField(max_length=500, null=True)
    deviceUUID = models.CharField(max_length=500, null=True)
    customerUUID = models.CharField(max_length=500, null=True)
    firstName = models.CharField(max_length=500, null=True)
    lastName = models.CharField(max_length=500, null=True)
    deviceTypeDescription = models.CharField(max_length=500, null=True)
    vin = models.CharField(max_length=500, null=True)
    make = models.CharField(max_length=500, null=True)
    model = models.CharField(max_length=500, null=True)
    year = models.CharField(max_length=500, null=True)
    driverId = models.CharField(max_length=500, null=True)
    groupId = models.CharField(max_length=500, null=True)
    eldVehicleId = models.CharField(max_length=500, null=True)

    class Meta:
        db_table='api_model_tracker_model'

class Location_Models(models.Model):
    imei = models.CharField(max_length=500, null=True)
    deviceUUID = models.CharField(max_length=500, null=True)
    deviceSerialNumber = models.CharField(max_length=500, null=True)
    driverId = models.CharField(max_length=500, null=True)
    firstName = models.CharField(max_length=500, null=True)
    lastName = models.CharField(max_length=500, null=True)
    personName = models.CharField(max_length=500, null=True)
    assetTracker = models.CharField(max_length=500, null=True)
    deviceReportTypeCode = models.CharField(max_length=500, null=True)
    latitude = models.CharField(max_length=500, null=True)
    longitude = models.CharField(max_length=500, null=True)
    heading = models.CharField(max_length=500, null=True)
    appDriverId = models.CharField(max_length=500, null=True)
    appDriverName = models.CharField(max_length=500, null=True)
    eldVehicleId = models.CharField(max_length=500, null=True)
    date = models.CharField(max_length=500, null=True)
    editDate = models.CharField(max_length=500, null=True)
    speed = models.CharField(max_length=500, null=True)
    speeding = models.CharField(max_length=500, null=True)
    behaviorCd = models.CharField(max_length=500, null=True)
    estSpeedLimit = models.CharField(max_length=500, null=True)
    fleetId = models.CharField(max_length=500, null=True)
    personMisc4 = models.CharField(max_length=500, null=True)
    personMisc5 = models.CharField(max_length=500, null=True)
    personMisc6 = models.CharField(max_length=500, null=True)
    personMisc7 = models.CharField(max_length=500, null=True)
    personMisc8 = models.CharField(max_length=500, null=True)
    vin = models.CharField(max_length=500, null=True)
    make = models.CharField(max_length=500, null=True)
    model = models.CharField(max_length=500, null=True)
    year = models.CharField(max_length=500, null=True)
    fuelLevel = models.CharField(max_length=500, null=True)
    battery = models.CharField(max_length=500, null=True)
    direction = models.CharField(max_length=500, null=True)
    trueOdo = models.CharField(max_length=500, null=True)
    virtualOdo = models.CharField(max_length=500, null=True)
    estimatedOdo = models.CharField(max_length=500, null=True)
    sensorData = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=500, null=True)

    class Meta:
        db_table='api_model_location_model'
