import random as rd
import copy
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

input_path = "input_files" # Input professors and classes
courses_path = os.path.join(input_path, "{}_{}_classes.csv".format(year, term))
instructors_path = os.path.join(input_path, "{}_{}_professors.csv".format(year, term))

class Schedule:
    def __init__(self, size=1000, mutation_rate=0.05, to_select=100, generations=200):
        # Initializing constants
        self.size = size
        self.mutation_rate = mutation_rate
        self.to_select = to_select
        self.gen = generations

        # Getting data from classes.csv and professors.csv
        self.courses = self.import_courses()
        self.instructors = self.import_instructors()
        self.seed = self.import_seed()

        self.solution = []
        self.final_fitness = 0

    def build(self):
        # Initial random population
        population = self.initialize_pop(self.size)

        selected_pop, top_fitness = [], 9999999999
        for k in range(self.gen):
            fit = [self.fitness(p) for p in population]
            selected_pop, top_fitness = self. select_top(population, fit)
            self.solution = copy.deepcopy(selected_pop[0])
            self.final_fitness = top_fitness
            print(k+1, top_fitness)
            if top_fitness == 0: break
            population = self. breed_population(selected_pop)

        #Save best solution
        self.export_schedule(self.solution)
        self.checkschedule()

    # Reading seed from last year
    def import_seed(self):
        return[]

    # Reading data from classes.csv
    def import_courses(self):
        courses = {}

        f = open(courses_path, 'r')
        f.readline()
        for l in f:
            # course ID, course name, professor name, type, location, course hour, houses, other requirements
            id, name, teacher, year_type, location, hour, house = l.strip().split(',')
            length = int(length)
            days = [int(d) for d in days.split(';') if d != '']
            starts = [int(s) for s in starts.split(';') if s != '']

            if courses.get(id) is None:
                courses[id] = [[name, teacher, year_type, location, hour, house]]
            else:
                courses[id].append([name, teacher, year_type, location, hour, house])
        f.close()
        return courses

    # Reading data from professors.csv
    def import_instructors(self):
        instructors = {}

        f = open(instructors_path, 'r')
        f.readline()
        for l in f:
            id, first_name, last_name, active = l.strip().split(',')
            length = int(length)
            days = [int(d) for d in days.split(';') if d != '']
            starts = [int(s) for s in starts.split(';') if s != '']

            if instructors.get(id) is None:
                instructors[id] = [[first_name, last_name, active]]
            else:
                instructors[id].append([first_name, last_name, active])
        f.close()
        return instructors

    # Generate all possible timeslots in chunks of chunks minutes
    def generate_timeslots(self):
         return time

    # Checks if a timeslot is available
    #def free_slot():
     #   return all

    # Initialize population of random schedules
    #def initialize_pop(self, size):
     #   return pop

    # Makes a random creature
    #def random_creature(self):
     #   return p

    # Fitness function for the schedule
    #def fitness(self, schedule):
     #   return fit 

    # Select top schedule
    def select_top(self, population, fitness):
        ind = sorted(range(len(population)), key=lambda k: fitness[k])
        return [copy.deepcopy(population[i]) for i in ind[:self.to_select]], fitness[ind[0]]


    #def breed_population(self, top_pop):
     #   return p

    #def print_schedule(self, schedule):
    #    print(s)

if __name__ == '__main__':
    s = Schedule()
    try:
        # s.import_schedule(schedule_path)
        # s.checkschedule()

    except IndexError:
        s.build()
        print("\nThe final fitness is {}".format(s.final_fitness))