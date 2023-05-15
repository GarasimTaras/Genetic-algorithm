import random
ELITE = 4

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
    for l in range(NUM):
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
     
    print(num1, num2) 
    temp = cycle[num1]
    cycle[num1] = cycle[num2]
    cycle[num2] = temp

def crossover(cycle1, cycle2, temp1, temp2):
    num1 = random.randrange(1, (NUM - 2))
    num2 = random.randrange((num1 + 1), (NUM - 1))

    node1_num, node2_num = 0, 0
    for i in range((num2 + 1), NUM):
        if (node_validation(cycle1[i], cycle2, num1, num2)):
            temp1[node1_num] = cycle1[i]
            node1_num += 1
        else:
            pass
        
        if (node_validation(cycle2[i], cycle1, num1, num2)):
            temp2[node2_num] = cycle2[i]
            node2_num += 1
        else:
            continue

    for j in range(num2 + 1):
        if (node_validation(cycle1[j], cycle2, num1, num2)):
            temp1[node1_num] = cycle1[j]
            node1_num += 1
        else:
            pass

        if (node_validation(cycle2[j], cycle1, num1, num2)):
            temp2[node2_num] = cycle2[j]
            node2_num += 1
        else:
            continue

    for n in range(num1, (num2 + 1)):
        temp = cycle1[n]
        cycle1[n] = cycle2[n]
        cycle2[n] = temp

    for k in range(num1):
        cycle1[k] = temp1[k]
        cycle2[k] = temp2[k]

    for l in range((num2 + 1), NUM):
        k += 1
        cycle1[l] = temp1[k]
        cycle2[l] = temp2[k]

    cycle1[NUM] = cycle1[0]
    cycle2[NUM] = cycle2[0]

def node_validation(node, swap, lower, upper):
    checksum = -1
    for i in range(lower, (upper + 1)):
        if (node != swap[i]):
            checksum += 1
        else:
            continue

    if (checksum == (upper - lower)):
        return True
    else:
        return False

#main program

NUM = get_length("cities.csv")

table = [[0 for j in range(NUM)]for i in range(NUM)]
cities = [0 for k in range(NUM)]

city_table("cities.csv", cities, table, NUM)


print_table(cities, table)


initial_num = int(factorial(NUM - 1))
solutions = [[0 for k in range(NUM + 1)] for l in range(initial_num)]

initial_pop(solutions, initial_num)


solutions_len = [fitness(solutions[i]) for i in range(initial_num)]

solution_sort(solutions, solutions_len)

temp1 = [-1 for i in range(NUM)]
temp2 = [-1 for j in range(NUM)]

crossover(solutions[5], solutions[25], temp1, temp2)
