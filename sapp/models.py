from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class driver_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    photo=models.FileField()
    email = models.CharField(max_length=100)
    regno=models.CharField(max_length=50)



class trafficpoolice_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    photo=models.FileField()
    designation=models.CharField(max_length=100)
    station=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)

class ambulance_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    vehicle_no = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    photo = models.FileField()
    proof = models.FileField()

class hospital_table(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image=models.FileField()

class accidentreport_table(models.Model):
    DRIVER = models.ForeignKey(driver_table, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=100)
    type=models.CharField(max_length=100)




class emargency_table(models.Model):
    ACCIDENTREPORT= models.ForeignKey(accidentreport_table, on_delete=models.CASCADE)
    HOSPITAL= models.ForeignKey(hospital_table, on_delete=models.CASCADE)
    AMBULANCE= models.ForeignKey(ambulance_table, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()


class location_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()


class complaint_table(models.Model):
    DRIVER = models.ForeignKey(driver_table, on_delete=models.CASCADE)
    TRAFFICPOLICE = models.ForeignKey(trafficpoolice_table, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)


class emergency_number(models.Model):
    DRIVER = models.ForeignKey(driver_table, on_delete=models.CASCADE)
    number=models.BigIntegerField()
    relation=models.CharField(max_length=100)





