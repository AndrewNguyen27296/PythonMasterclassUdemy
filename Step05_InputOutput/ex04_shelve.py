import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = 'a sweet, orange, citrus fruit'
    fruit['apple'] = 'good for making cider'
    fruit['lemon'] = 'a sour, yellow citrus fruit'
    fruit['grape'] = 'a small. sweet fruit growing in bunches'
    fruit['lime'] = 'a sour, green citrus fruit'

    print(fruit['lemon'])
    print(fruit['grape'])

    while True:
        shelve_key = input("Please enter a fruit: ")
        if shelve_key == 'quit':
            break

        if shelve_key in fruit:
            description = fruit.get(shelve_key)
            print(description)
        else:
            print("We don't have a " + shelve_key)


