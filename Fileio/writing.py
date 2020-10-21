# cities = ["A", "B", "C"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# with open("cities.txt", 'r') as cities:
#     cities = cities.readlines()
#     for city in cities:
#         print(city, end='')

cities = []

with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))
print(cities)
for city in cities:
    print(city)