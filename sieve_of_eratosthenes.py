numbers = []
status = ["composite"]
for i in range(1, 101):
    numbers.append(i)

for i in range(1, 100):
    status.append("unchecked")

for a in range(0, 100):
    if status[a] == "unchecked":
        prime = numbers[a]
        status[a] = "prime"
        for b in range(numbers[a], 100 // prime + 1):
            status[b * prime - 1] = "composite"

for i in range(0, 100):
    if status[i] == "prime":
        print(numbers[i])