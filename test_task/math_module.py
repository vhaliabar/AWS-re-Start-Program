import math
import random
y = random.random()
print(y)

x = random.choice([i for i in range(0,10) if i%3==0 or i%5==0])
print(x)

heads_total = 35
legs_total = 94
legsInOneChicken = 2
legsInOneRabbit = 4
for head in range(1, int(heads_total)):
    if (head*legsInOneChicken + ((heads_total-head)*legsInOneRabbit)) == 94:
        print(f'chickens: {head}, rebbits: {heads_total-head}')