import random as rd
import time
import os
# import create_schedule as cs
# import mysql_requests as mysql


year = 2020
term = 4

timestamp = int(time.time())
def htoMin(hour,minutes):
    return hour*60+minutes

def texttoMin(time):
    h, m = map(int, time.split(':'))
    return htoMin(h,m)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
chunks = 30 # Size of the time slots
start_day = htoMin(9,0)
end_day = htoMin(17,30)

input_path = "input_files" # input professors and classes
courses_path = os.path.join(input_path, "{}_{}_classes.csv".format(year, term))
instructors_path = os.path.join(input_path, "{}_{}_professors.csv".format(year, term))