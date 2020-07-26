from django.shortcuts import render
from sqlserverconnect.models import profsqlserverconn
import pyodbc

def home(request):
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

