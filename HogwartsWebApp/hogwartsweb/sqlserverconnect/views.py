from django.shortcuts import render
from sqlserverconnect.models import profsqlserverconn
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
        if request.POST.get('ProfessorID') and request.POST.get('LastName') and request.POST.get('FirstName') and request.POST.get('Active'):
            insertvalues=profsqlserverconn()
            insertvalues.ProfessorID = request.POST.get('ProfessorID')
            insertvalues.LastName = request.POST.get('LastName')
            insertvalues.FirstName = request.POST.get('FirstName')
            insertvalues.Active = request.POST.get('Active')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Professors VALUES ('"+insertvalues.ProfessorID+"', '"+insertvalues.LastName+"', '"+insertvalues.FirstName+"', '"+insertvalues.Active+"')")
            cursor.commit()
            return render(request,'profAdd.html')
    else:
        return render(request, 'profAdd.html')
        