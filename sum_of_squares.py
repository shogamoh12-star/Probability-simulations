import random
dimensions = 3
total_valid = 0
sample_size = 1000
for j in range(0, sample_size):
    sum = 0
    variables = []
    for i in range(0, dimensions):
        variables.append(random.random())

    for i in variables:
        sum += i ** 2

    if sum <= 1:
        total_valid += 1

print(str(total_valid))