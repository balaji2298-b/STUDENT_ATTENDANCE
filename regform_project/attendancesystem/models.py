from django.db import models



class Formpage(models.Model):
    serial_no = models.CharField(max_length=3)
    studentsname = models.CharField(max_length=100)
    contactnumber = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    intime = models.CharField(max_length=8)
    outtime = models.CharField(max_length=8)
    pre = models.CharField(max_length=10)
    abe = models.CharField(max_length=10)
    inform = models.CharField(max_length=10)

