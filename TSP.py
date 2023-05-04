


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

get_length("cities.csv")
city_table("cities.csv", NUM)
print_table(cities, table)