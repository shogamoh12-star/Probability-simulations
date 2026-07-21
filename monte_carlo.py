import random
import math
in_circle = 0

total = 1000000

for i in range(0, total):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if math.sqrt(x**2 + y**2) <= 1:
        in_circle = in_circle + 1

print("Total in circle: " + str(in_circle))
print(in_circle / total * 4)