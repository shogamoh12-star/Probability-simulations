import matplotlib.pyplot as plt
import random

rounds = 5000
number_of_players = 2000
p_values = []
records = []
at_bar = []
limit = number_of_players * 0.6
number_of_people_in_bar = 0
crowded = False
tolerance = -5
m = 2
crib_sheet = []
prediction = True
pattern = []

for i in range(0, number_of_players):
    p = random.uniform(0, 1)
    p_values.append(p)
    records.append(0)
    at_bar.append(False)

for x in range(0, rounds):

    # Check and update p values as needed
    for i in range(0, number_of_players):
        if records[i] == tolerance:
            p_values[i] = random.uniform(0, 1)
            records[i] = 0

    # generate from the crib sheet
    pattern = []
    if len(crib_sheet) >= m:
        for i in range(len(crib_sheet) - m, len(crib_sheet)):
            pattern.append(crib_sheet[i])

    # now search for the last time this pattern occurred (once per round, not once per player)
    found = False
    length = len(crib_sheet)
    for i in range(0, length - m):
        segment = crib_sheet[i:i + m]
        if segment == pattern:
            prediction = crib_sheet[i + m]
            found = True

    # Generate decision based on prediction and p values
    for i in range(0, number_of_players):
        if not found:
            rand = random.randint(1, 2)
            if rand == 1:
                prediction = True
            else:
                prediction = False
        rand = random.uniform(0, 1)
        if rand <= p_values[i]:
            at_bar[i] = prediction
        else:
            at_bar[i] = not prediction

    # Calculate number of people who are at the bar
    number_of_people_in_bar = 0
    for i in range(0, number_of_players):
        if at_bar[i] == True:
            number_of_people_in_bar += 1

    # Calculate whether bar is crowded or not
    if number_of_people_in_bar > limit:
        crowded = True
    else:
        crowded = False
    crib_sheet.append(not crowded)

    # Update players' records
    for i in range(0, number_of_players):
        if at_bar[i] == crib_sheet[x]:
            records[i] += 1
        else:
            records[i] -= 1

print(p_values)
plt.hist(p_values, bins=50, edgecolor="black")
plt.xlabel("p value")
plt.ylabel("Frequency")
plt.title("Distribution of player p values")
plt.savefig("p_value_histogram_2.png", dpi=150, bbox_inches="tight")
plt.show()
