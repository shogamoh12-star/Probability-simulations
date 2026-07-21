import math
def find_factors(n):
    factors_list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            factors_list.append(i)
            if (n / i != i):
                factors_list.append(int(n / i))
    return factors_list
 
total = 0

for i in range(1, 1000000):
    if(len(find_factors(i)) == 2):
        total += 1

print(total)

