import random
avg = 0
trials = 100000
for i in range(0, trials):
    number_of_cards = 10
    cards = []
    for i in range(0, number_of_cards):
        cards.append(i)
    number_of_packs = 0
    collected = []
    while len(collected) < number_of_cards:
        new_card = random.randint(0, number_of_cards - 1)
        if cards[new_card] != -1:
            collected.append(cards[new_card])
            cards[new_card] = -1
        number_of_packs += 1
    avg += number_of_packs

print("average: " + str(avg / trials))