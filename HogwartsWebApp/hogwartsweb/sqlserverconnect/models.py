from django.db import models

#GET Professor Database
class profsqlserverconn(models.Model):
    ProfessorID = models.IntegerField()
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    Active = models.IntegerField()

#GET Student Database
class studentsqlserverconn(models.Model):
    StudentID = models.IntegerField()
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    HouseID = models.IntegerField()
    Year = models.IntegerField()
    ElectiveOneID = models.IntegerField()
    ElectiveTwoID = models.IntegerField()

#GET Classes Database
class classessqlserverconn(models.Model):
    ClassId = models.IntegerField()
    Name = models.CharField(max_length=100)
    Year1Type = models.IntegerField()
    Year2Type = models.IntegerField()
    Year3Type = models.IntegerField()
    Year4Type = models.IntegerField()
    Year5Type = models.IntegerField()
    Year6Type = models.IntegerField()
    Year7Type = models.IntegerField()
    Location = models.CharField(max_length=100)
    MaxCapacity = models.IntegerField()
    NumberofHouses = models.IntegerField()

class schedulesqlserverconn(models.Model):
    ScheduledClassID = models.IntegerField()
    ProfessorClassID = models.IntegerField()
    HouseID = models.IntegerField()
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    DaysoftheWeek = models.CharField(max_length=100)
    Year = models.IntegerField()
    MaxOccupancy = models.IntegerField()
    Occupancy = models.IntegerField()
    RemainingSpots = models.IntegerField()
    Location = models.CharField(max_length=100)
    NumberofHouses = models.IntegerField()