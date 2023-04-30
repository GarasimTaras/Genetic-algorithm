



def get_length(names):
    global NUM
    f = open(names, "r")
    temp = f.readline()
    temp = temp.replace(",", "")
    NUM = len(temp) - 1
    f.close()

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

def print_table(names, distance):
    print("  ", end="")
    for i in range(NUM):
        print(f"{names[i]}", end=",")
    print("")
    for p in range(NUM):
        print(f"{names[p]}", end=",")
        for r in range(NUM):
            print(f"{distance[p][r]}", end=",")

        print("")

get_length("cities.csv")
city_table("cities.csv", NUM)
print_table(cities, table)