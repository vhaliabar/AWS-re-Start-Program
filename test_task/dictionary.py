countries = ['Ukraine', 'France', 'Germany', 'Netherlands']
cities = ['Lviv', 'Paris', 'Berlin', 'Amsterdam']

capitals = dict()

for i in range(len(cities)):
    capitals[countries[i]]=cities[i]

print(capitals.get('Germany'))
print(capitals)