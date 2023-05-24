#copyright
import random
import sys
ELITE = 4

#Function to get number on cities inputed
def get_length(names):
    num = 0
    f = open(names, "r")
    temp = f.readline().strip('\n')
    temp = temp.split(',')
    num = len(temp)
    f.close()
    return num

#Function to create 2D array with distances between cities
#And 1D array with names of the cities
def city_table(file, names, distance, num):
    f = open(file, "r")
    text = f.readline().strip('\n')
    
    for name in range(num):
        names[name] = text.split(',')[name]

    for row in range(num):
        text = f.readline().strip('\n')
        for column in range(num):
            distance[row][column] = text.split(',')[column]

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
    num1 = random.randrange(0, NUM + 1)
    num2 = random.randrange(0, NUM + 1)
    while (num1 == num2):
        num2 = random.randrange(1, NUM)
    
    temp = cycle[num1]
    cycle[num1] = cycle[num2]
    cycle[num2] = temp

    if ((num1 == 0) or (num2 == 0)):
        cycle[NUM] = cycle[0]
    elif ((num1 == NUM) or (num2 == NUM)):
        cycle[0] = cycle[NUM]
    

def crossover(solu1, solu2, new1, new2):
    num1 = random.randrange(1, (NUM - 2))
    num2 = random.randrange((num1 + 1), (NUM - 1))

    for swap in range(num1, num2 + 1):
        temp_array[new2][swap] = solutions[solu1][swap]
        temp_array[new1][swap] = solutions[solu2][swap]
    
    node1_filled = 0
    node2_filled = 0

    for fill in range(num2 + 1, NUM):
        if (node_validation(solutions[solu1][fill], temp_array[new1], num1, num2)):
            temp_array[new1][node1_filled] = solutions[solu1][fill]
            node1_filled += 1
            if (node1_filled == num1):
                node1_filled = num2 + 1

        if (node_validation(solutions[solu2][fill], temp_array[new2], num1, num2)):
            temp_array[new2][node2_filled] = solutions[solu2][fill]
            node2_filled += 1
            if (node2_filled == num1):
                node2_filled = num2 + 1
        

    for fill in range(0, num2 + 1):
        if (node_validation(solutions[solu1][fill], temp_array[new1], num1, num2)):
            temp_array[new1][node1_filled] = solutions[solu1][fill]
            node1_filled += 1
            if (node1_filled == num1):
                node1_filled = num2 + 1

        if (node_validation(solutions[solu2][fill], temp_array[new2], num1, num2)):
            temp_array[new2][node2_filled] = solutions[solu2][fill]
            node2_filled += 1
            if (node2_filled == num1):
                node2_filled = num2 + 1
            

    temp_array[new1][NUM] = temp_array[new1][0]
    temp_array[new2][NUM] = temp_array[new2][0]



def node_validation(node, array, lower, upper):
    checksum = -1
    for i in range(lower, (upper + 1)):
        if (node != array[i]):
            checksum += 1
        else:
            continue

    if (checksum == (upper - lower)):
        return True
    else:
        return False

def tournament(iter_num):
    if (iter_num == 1):
        cycle1 = random.randrange(0, initial_num)
        cycle2 = random.randrange(0, initial_num)

        parent1 = solutions_len[cycle1]
        parent2 = solutions_len[cycle2]

        if (parent1 < parent2):
            return cycle1, iter_num
        else:
            return cycle2, iter_num
    else:
        iter_num -= 1
        cycle1 = tournament(iter_num)[0]
        cycle2 = tournament(iter_num)[0]

        parent1 = solutions_len[cycle1]
        parent2 = solutions_len[cycle2]

        if (parent1 < parent2):
            return cycle1, iter_num
        else:
            return cycle2, iter_num    


def print_solution(cycle,cities):
    for node in range(NUM + 1):
        print(f"{cities[cycle[node]]}", end=",")
    print()

#main program




NUM = get_length(sys.argv[1])

table = [[0 for j in range(NUM)]for i in range(NUM)]
cities = [0 for k in range(NUM)]

city_table(sys.argv[1], cities, table, NUM)

print_table(cities, table)

initial_num = int(factorial(NUM - 1) / 5)
if (int(factorial(NUM - 1) / 5) > 200):
    initial_num = 200
else:
    pass

solutions = [[0 for k in range(NUM + 1)] for l in range(initial_num)]

initial_pop(solutions, initial_num)

solutions_len = [fitness(solutions[i]) for i in range(initial_num)]

solution_sort(solutions, solutions_len)

temp_array = [[0 for k in range(NUM + 1)] for l in range(initial_num)]



for i in range(int(sys.argv[3])):
    for n in range(ELITE):
        temp_array[n] = solutions[n]
            
    for m in range(ELITE, initial_num, 2):
        crossover(tournament(int(sys.argv[2]))[0],tournament(int(sys.argv[2]))[0], m, (m + 1))

        if ((random.randrange(1,26) / 25) == 1):
            mutation(temp_array[m])

        if ((random.randrange(1,26) / 25) == 1):
            mutation(temp_array[m + 1])

 
    for solu in range(initial_num):
        for node in range(NUM + 1):
            solutions[solu][node] = temp_array[solu][node]
   

    for cycle in range(initial_num):
        solutions_len[cycle] = fitness(solutions[cycle])
        solution_sort(solutions, solutions_len)  
        
    print(f"{i + 1}:", solutions_len[0])

 

print()
print_solution(solutions[0], cities)
print(solutions_len[0])