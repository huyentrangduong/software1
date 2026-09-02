
cities = []
city = input("enter the name of five city: ")
city_round = 5
finished_round = 0


while finished_round < city_round:
    cities.append(city)
    city = input("enter the name of five city: ")
print ("The cities you entered: ")
finished_rounds += 1


for n in cities:
    print(n[1:6])