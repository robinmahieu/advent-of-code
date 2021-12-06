with open("input.txt") as f:
    data = f.read().split(",")

fish = list(map(int, data))

for _ in range(80):
    fish = [timer - 1 for timer in fish]

    for index, timer in enumerate(fish):
        if timer == -1:
            fish[index] = 6
            fish.append(8)

amount = len(fish)

print(amount)
