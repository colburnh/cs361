from django.shortcuts import render
from sqlserverconnect.models import profsqlserverconn
from sqlserverconnect.models import studentsqlserverconn
from sqlserverconnect.models import classessqlserverconn
import pyodbc

#Request for index
def index(request):
    return render(request, 'index.html')


#Request for Professor
def profconnsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                        'Database=HogwartsDatabase;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Professors")
    result=cursor.fetchall()
    return render(request,'professor.html',{'profsqlserverconn':result})

#Request for Student
def studentconnsql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    result = cursor.fetchall()
    return render(request, 'student.html', {'studentsqlserverconn': result})

#Request for Classes
def classesconnsql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Classes")
    result = cursor.fetchall()
    return render(request, 'classes.html', {'classessqlserverconn': result})

#Request for Scheduled Classes
def scheduleconnsql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ScheduledClasses")
    result = cursor.fetchall()
    return render(request, 'schedule.html', {'schedulesqlserverconn': result})


def profAdd(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    if request.method=="POST":
        if request.POST.get('LastName') and request.POST.get('FirstName') and request.POST.get('Active'):
            insertvalues=profsqlserverconn()
            insertvalues.LastName = request.POST.get('LastName')
            insertvalues.FirstName = request.POST.get('FirstName')
            insertvalues.Active = request.POST.get('Active')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Professors VALUES ('"+insertvalues.LastName+"', '"+insertvalues.FirstName+"', '"+insertvalues.Active+"')")
            cursor.commit()
            return render(request, 'profAdd.html')
    else:
        return render(request, 'profAdd.html')

def classesAdd(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    if request.method=="POST":
        if request.POST.get('Name'):
            insertvalues=classessqlserverconn()
            insertvalues.Name = request.POST.get('Name')
            insertvalues.Year1Type = request.POST.get('Year1Type')
            insertvalues.Year2Type = request.POST.get('Year2Type')
            insertvalues.Year3Type = request.POST.get('Year3Type')
            insertvalues.Year4Type = request.POST.get('Year4Type')
            insertvalues.Year5Type = request.POST.get('Year5Type')
            insertvalues.Year6Type = request.POST.get('Year6Type')
            insertvalues.Year7Type = request.POST.get('Year7Type')
            insertvalues.Location = request.POST.get('Location')
            insertvalues.MaxCapacity = request.POST.get('MaxCapacity')
            insertvalues.NumberofHouses = request.POST.get('NumberofHouses')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Classes VALUES ('"+insertvalues.Name+"', '"+insertvalues.Year1Type+"', '"+insertvalues.Year2Type+"','"+insertvalues.Year3Type+"' ,'"+insertvalues.Year4Type+"' ,'"+insertvalues.Year5Type+"' ,'"+insertvalues.Year6Type+"' ,'"+insertvalues.Year7Type+"''"+insertvalues.Location+"', '"+insertvalues.MaxCapacity+"' , '"+insertvalues.NumberofHouses+"')")
            cursor.commit()
            return render(request, 'classesAdd.html')
    else:
        return render(request, 'classesAdd.html')

def studentAdd(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=DESKTOP-13TEU52\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    if request.method=="POST":
        if request.POST.get('LastName') and request.POST.get('FirstName'):
            insertvalues=studentsqlserverconn()
            insertvalues.LastName = request.POST.get('LastName')
            insertvalues.FirstName = request.POST.get('FirstName')
            insertvalues.HouseID = request.POST.get('HouseID')
            insertvalues.Year = request.POST.get('Year')
            insertvalues.ElectiveOneID = request.POST.get('ElectiveOneID')
            insertvalues.ElectiveOTwoID = request.POST.get('ElectiveOTwoID')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Students VALUES ('"+insertvalues.LastName+"', '"+insertvalues.FirstName+"', '"+insertvalues.HouseID+"','"+insertvalues.Year+"')")
            cursor.commit()
            return render(request, 'studentAdd.html')
    else:
        return render(request, 'studentAdd.html')
        