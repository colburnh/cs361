from django.shortcuts import render
from sqlserverconnect.models import profsqlserverconn
from sqlserverconnect.models import studentsqlserverconn
from sqlserverconnect.models import classessqlserverconn
import pyodbc

#Request for index
def index(request):
    return render(request, 'index.html')

def connect():
    #  Used to create connection to the database
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=DESKTOP-UD435N0\SQLEXPRESS;'
                          'Database=HogwartsDatabase;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    return cursor

#Request for Professor
def profconnsql(request):
    cursor = connect()
    cursor.execute("EXECUTE dbo.usp_get_professors")
    result=cursor.fetchall()
    return render(request,'professor.html',{'profsqlserverconn':result})

#Request for Student
def studentconnsql(request):
    cursor = connect()
    cursor.execute("EXECUTE dbo.usp_get_students")
    result = cursor.fetchall()
    return render(request, 'student.html', {'studentsqlserverconn': result})

#Request for Classes
def classesconnsql(request):
    cursor = connect()
    cursor.execute("EXECUTE dbo.usp_get_classes")
    result = cursor.fetchall()
    return render(request, 'classes.html', {'classessqlserverconn': result})

#Request for Scheduled Classes
def scheduleconnsql(request):
    cursor = connect()
    cursor.execute("EXECUTE dbo.usp_get_scheduledclasses @year='1'")
    result1 = cursor.fetchall()
    cursor.execute("EXECUTE dbo.usp_get_scheduledclasses @year='2'")
    result2 = cursor.fetchall()
    cursor.execute("EXECUTE dbo.usp_get_scheduledclasses @year='3'")
    result3 = cursor.fetchall()
    cursor.execute("EXECUTE dbo.usp_get_scheduledclasses @year='4'")
    result4 = cursor.fetchall()
    cursor.execute("EXECUTE dbo.usp_get_scheduledclasses @year='5'")
    result5 = cursor.fetchall()

    context = {'year1':result1, 'year2':result2, 'year3':result3, 'year4':result4, 'year5':result5}


    return render(request, 'schedule.html', context)


def profAdd(request):
    if request.method=="POST":
        if request.POST.get('LastName') and request.POST.get('FirstName') and request.POST.get('Active'):
            insertvalues=profsqlserverconn()
            insertvalues.LastName = request.POST.get('LastName')
            insertvalues.FirstName = request.POST.get('FirstName')
            insertvalues.Active = request.POST.get('Active')
            cursor = connect()
            cursor.execute("EXECUTE usp_insert_professor @firstName='"
                           +insertvalues.LastName+ "', @LastName='"
                           +insertvalues.FirstName+ "', @Active='"
                           +insertvalues.Active+ "'")
            cursor.commit()
            return render(request, 'profAdd.html')
    else:
        return render(request, 'profAdd.html')

def classesAdd(request):
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
            cursor = connect()
            cursor.execute("EXECUTE usp_insert_class @Name='"
                            +insertvalues.Name+"', @Year1Type='"
                            +insertvalues.Year1Type+"', @Year2Type='"
                            +insertvalues.Year2Type+"', @Year3Type='"
                            +insertvalues.Year3Type+"', @Year4Type='"
                            +insertvalues.Year4Type+"', @Year5Type='"
                            +insertvalues.Year5Type+"', @Year6Type='"
                            +insertvalues.Year6Type+"', @Year7Type='"
                            +insertvalues.Year7Type+"',@Location='"
                            +insertvalues.Location+"', @MaxCapacity='"
                            +insertvalues.MaxCapacity+"', @numberOfHouses='"
                            +insertvalues.NumberofHouses+"'")
            cursor.commit()
            return render(request, 'classesAdd.html')
    else:
        return render(request, 'classesAdd.html')

def studentAdd(request):
    if request.method=="POST":
        if request.POST.get('LastName') and request.POST.get('FirstName'):
            insertvalues=studentsqlserverconn()
            insertvalues.LastName = request.POST.get('LastName')
            insertvalues.FirstName = request.POST.get('FirstName')
            insertvalues.HouseID = request.POST.get('HouseID')
            insertvalues.Year = request.POST.get('Year')
            insertvalues.ElectiveOneID = request.POST.get('ElectiveOneID')
            insertvalues.ElectiveOTwoID = request.POST.get('ElectiveOTwoID')
            cursor = connect()
            cursor.execute("EXECUTE usp_insert_student @LastName='"
                            +insertvalues.LastName+ "', @FirstName='"
                            +insertvalues.FirstName+ "', @HouseID='"
                            +insertvalues.HouseID+ "', @Year='"
                            +insertvalues.Year+ "', @ElectiveOneID='"
                            +insertvalues.ElectiveOneID+ "', @ElectiveTwoID='"
                            +insertvalues.ElectiveOTwoID+ "'")
            cursor.commit()
            return render(request, 'studentAdd.html')
    else:
        return render(request, 'studentAdd.html')
    
#delete functions
def delete_professor(request,pk):

    context = {"item":pk}
	
    if request.method == "POST":
        cursor = connect()
        cursor.execute("EXECUTE usp_delete_professor @ProfessorID='"
                        +str(pk)+ "'")
        cursor.commit()
        return profconnsql(request)

    return render(request, 'profDelete.html', context)

def delete_student(request,pk):

    context = {"item":pk}
	
    if request.method == "POST":
        cursor = connect()
        cursor.execute("EXECUTE usp_delete_student @StudentID='"
                        +str(pk)+ "'")
        cursor.commit()
        return studentconnsql(request)

    return render(request, 'studentDelete.html', context)

def delete_classes(request,pk):

    context = {"item":pk}
	
    if request.method == "POST":
        cursor = connect()
        cursor.execute("EXECUTE usp_delete_class @ClassID='"
                        +str(pk)+ "'")
        cursor.commit()
        return classesconnsql(request)

    return render(request, 'classDelete.html', context)
