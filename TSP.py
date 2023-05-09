import random
#ELITE_NUM = 5



#Function to get number on cities inputed
def get_length(names):
    global NUM
    f = open(names, "r")
    temp = f.readline()
    temp = temp.replace(",", "")
    NUM = len(temp) - 1
    f.close()

#Function to create 2D array with distances between cities
#And 1D array with names of the cities
def city_table(names, num):
    global cities
    global table

    f = open(names, "r")
    text = f.readline()

    table = [[0 for j in range(num)]for i in range(num)]
    cities = [text[i * 2] for i in range(num)]

    for p in range(num):
        text = f.readline()
        for r in range(num):

            table[p][r] = text[2 * r]

    f.close()

#Function to print city table 
def print_table(names, distance):
    print("  ", end="")
    #Prints first row with names of all cities
    for i in range(NUM):
        print(f"{names[i]}", end=",")
    print("")
    #prints Name of the city and distance to all other cities
    for p in range(NUM):
        print(f"{names[p]}", end=",")
        for r in range(NUM):
            print(f"{distance[p][r]}", end=",")

        print("")
        
#def test():
    #for x in range(ELITE_NUM):
        #solution(x) 

def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num - 1)

def create_cycle():
    solution = [0 for i in range(NUM)]
    temp_cities = [(j) for j in range(NUM)]
    for l in range(NUM ):
        rand_num = random.randrange(0, NUM - l)
        solution[l] = temp_cities[rand_num]
        temp_cities.pop(rand_num)

    solution.insert(NUM, solution[0])
    return solution


def initial_pop():
    global initial_num
    initial_num = int(factorial(NUM - 1) / 5)
    global solutions
    solutions = [[0 for k in range(NUM + 1)] for l in range(initial_num)]

    for n in range(initial_num):
        array = create_cycle()
        for m in range(NUM + 1):
            solutions[n][m] = array[m]

def fitness(solution):
    lenght = 0
    for i in range(NUM):
        lenght = lenght + int(table[solution[i]][solution[i + 1]])
    
    return lenght
  

get_length("cities.csv")
city_table("cities.csv", NUM)
print_table(cities, table)
initial_pop()
solution_len = [fitness(solutions[i]) for i in range(initial_num)]
print(solution_len)