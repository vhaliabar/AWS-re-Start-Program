import math
import random
y = random.random()
print(y)

#random number from 0 to 100 inclusive, which is divisible by 5 and 7
firstInRange=0
lastInRange = 100
x = random.choice([i for i in range(firstInRange,lastInRange+1) if i%3==0 and i%5==0])
print(x)

#classic ancient Chinese puzzle(rabbits and chickens)
heads_total = 35
legs_total = 94
legsInOneChicken = 2
legsInOneRabbit = 4
for head in range(1, int(heads_total)):
    if (head*legsInOneChicken + ((heads_total-head)*legsInOneRabbit)) == legs_total:
        print(f'chickens: {head}, rabbits: {heads_total-head}')