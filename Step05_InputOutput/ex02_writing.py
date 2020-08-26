cities = ["Koln", "Munchen", "Hangover"]

with open('cities.txt', 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
# if file is not exist, it will create new
# if it existed, it will be overwritten