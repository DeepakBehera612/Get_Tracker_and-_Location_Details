from django.shortcuts import render
from api_tracker.models import Tracker_Models, Location_Models
import requests
import psycopg2
import configparser



con = psycopg2.connect(user="postgres", password="admin",
                       host="localhost", port="5432", database="db_tracker_location")

con.autocommit = True
config = configparser.ConfigParser()
config.read('config.ini')
key = config.get('token', 'key')
base_url = config.get('token', 'base_url')
headers = {
    'Authorization': key
}

tracker_response = requests.request("GET", base_url+'/tracker',
                                    headers=headers).json()

location_response = requests.request(
    "GET", base_url+'/locations', headers=headers).json()

def show_tracker_data_from_db(request):
    tracker_result = Tracker_Models.objects.all()
    return render(request, 'tracker.html', {'tracker_response': tracker_result})

def tracker_button(request):
    return render(request, 'tracker.html')

def insert_tracker_data_todb(request):
    id = 0
    for i in tracker_response:      
        id += 1 
        imei = str(i['imei'])
        deviceUUID = str(i['deviceUUID'])
        customerUUID = str(i['customerUUID'])
        firstName = str(i['firstName'])
        lastName = str(i['lastName'])
        deviceTypeDescription = str(i['deviceTypeDescription'])
        vin = str(i['vin'])
        make = str(i['make'])
        model = str(i['model'])
        year = str(i['year'])
        eldVehicleId = str(i['eldVehicleId'])
        driverId = str(i['driverId'])
        groupId = str(i['groupId'])
        cursor = con.cursor()
        insert_query = """INSERT INTO api_model_tracker_model VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (id,imei, deviceUUID, customerUUID, firstName, lastName,
                            deviceTypeDescription, vin, make, model, year, eldVehicleId, driverId, groupId)
        cursor.execute(insert_query, record_to_insert)
        cursor = con.cursor()
        con.commit()
    return render(request, 'success.html')


# implement location

def show_location_data_from_db(request, id):
    cursor = con.cursor()
    postgreSQL_select_Query = f"select * from api_model_location_model where imei='{id}'"
    cursor.execute(postgreSQL_select_Query)
    get_id_records = cursor.fetchone()
    return render(request, "location.html", {'get_id_records': get_id_records})


def location_button(request):
    return render(request, 'location.html')


def insert_locations_data_todb(request):
    id = 0
    for j in location_response['data']['locations']:
        id += 1
        imei = str(j['imei'])
        deviceUUID = str(j['deviceUUID'])
        deviceSerialNumber = str(j['deviceSerialNumber'])
        driverId = str(j['driverId'])
        firstName = str(j['firstName'])
        lastName = str(j['lastName'])
        personName = str(j['personName'])
        assetTracker = str(j['assetTracker'])
        deviceReportTypeCode = str(j['deviceReportTypeCode'])
        latitude = str(j['latitude'])
        longitude = str(j['longitude'])
        heading = str(j['heading'])
        appDriverId = str(j['appDriverId'])
        appDriverName = str(j['appDriverName'])
        eldVehicleId = str(j['eldVehicleId'])
        date = str(j['date'])
        editDate = str(j['editDate'])
        speed = str(j['speed'])
        speeding = str(j['speeding'])
        behaviorCd = str(j['behaviorCd'])
        estSpeedLimit = str(j['estSpeedLimit'])
        fleetId = str(j['fleetId'])
        personMisc4 = str(j['personMisc4'])
        personMisc5 = str(j['personMisc5'])
        personMisc6 = str(j['personMisc6'])
        personMisc7 = str(j['personMisc7'])
        personMisc8 = str(j['personMisc8'])
        vin = str(j['vin'])
        make = str(j['make'])
        model = str(j['model'])
        year = str(j['year'])
        fuelLevel = str(j['fuelLevel'])
        battery = str(j['battery'])
        direction = str(j['direction'])
        trueOdo = str(j['trueOdo'])
        virtualOdo = str(j['virtualOdo'])
        estimatedOdo = str(j['estimatedOdo'])
        sensorData = str(j['sensorData'])
        status = str(j['status'])
        
        cursor = con.cursor()
        location_insert_query = """INSERT INTO api_model_location_model VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (id,imei, deviceUUID, deviceSerialNumber, driverId, firstName, lastName, personName, assetTracker, deviceReportTypeCode, latitude, longitude, heading, appDriverId, appDriverName, eldVehicleId, date, editDate,
                            speed, speeding, behaviorCd, estSpeedLimit, fleetId, personMisc4, personMisc5, personMisc6, personMisc7, personMisc8, vin, make, model, year, fuelLevel, battery, direction, trueOdo, virtualOdo, estimatedOdo, sensorData, status)
        cursor.execute(location_insert_query, record_to_insert)
        con.commit()
    return render(request, 'success.html')
