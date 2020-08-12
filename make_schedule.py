import random as rd
import os

def make_schedule(year, term, csv_courses, csv_schedule):
    try:
        sch = open(csv_schedule, 'r')
    except IOError:
        print("Please enter a valid path for the CSV schedule")
        exit()

    try:
        crs = open(csv_courses, 'r')
    except IOError:
        print("Please enter a valid path for the CSV courses")
        exit()

schedule_path = csv_schedule.replace("csv", "tex")

title = "Timetable for Year {}/{}, Term {}".format(year,year+1,term)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
chunks = 30
start_day = 9*60
end_day = 18*60