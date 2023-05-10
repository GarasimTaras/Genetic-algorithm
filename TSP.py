import random


#Function to get number on cities inputed
def get_length(names):
    num = 0
    f = open(names, "r")
    temp = f.readline()
    temp = temp.replace(",", "")
    num = len(temp) - 1
    f.close()
    return num

#Function to create 2D array with distances between cities
#And 1D array with names of the cities
def city_table(file, names, distance, num):
    f = open(file, "r")
    text = f.readline()

    for i in range(num):
        names[i] = text[i * 2]

    for p in range(num):
        text = f.readline()
        for r in range(num):
            distance[p][r] = text[2 * r]

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

def initial_pop(cycles, num):
    for n in range(num):
        array = create_cycle()
        for m in range(NUM + 1):
            cycles[n][m] = array[m]

def fitness(cycle):
    lenght = 0
    for i in range(NUM):
        lenght = lenght + int(table[cycle[i]][cycle[i + 1]])
    
    return lenght

def solution_sort(cycles, len_array):
    for i in range(initial_num - 2):
        for j in range(initial_num - 1):
            if (len_array[j] > len_array[j + 1]):
                temp = len_array[j]
                len_array[j] = len_array[j + 1]
                len_array[j + 1] = temp

                temp = cycles[j]
                cycles[j] = cycles[j + 1]
                cycles[j + 1] = temp
            else:
                continue

def mutation(cycle):
    num1 = random.randrange(0, NUM)
    num2 = random.randrange(0, NUM)
    while (num1 == num2):
        num2 = random.randrange(0, NUM)
    
    temp = cycle[num1]
    cycle[num1] = cycle[num2]
    cycle[num2] = temp


#main program

NUM = get_length("cities.csv")

table = [[0 for j in range(NUM)]for i in range(NUM)]
cities = [0 for k in range(NUM)]

city_table("cities.csv", cities, table, NUM)


print_table(cities, table)


initial_num = int(factorial(NUM - 1) / 5)
solutions = [[0 for k in range(NUM + 1)] for l in range(initial_num)]

initial_pop(solutions, initial_num)


solutions_len = [fitness(solutions[i]) for i in range(initial_num)]

solution_sort(solutions, solutions_len)

