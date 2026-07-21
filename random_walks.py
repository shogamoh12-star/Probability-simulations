import random
import math
position = 0
for i in range(0, 100):
    direction = random.randint(1, 2)
    if direction == 2:
        position += 1
    else:
        position -= 1
    print(str(position))

print("Final position: " + str(position))