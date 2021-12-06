with open("input.txt") as f:
    data = f.read().split(",")

original_fish = list(map(int, data))

fish = [0] * 10

for timer in original_fish:
    fish[timer + 1] += 1

for _ in range(256):
    fish.append(fish.pop(0))

    fish[7] += fish[0]
    fish[9] += fish[0]

    fish[0] = 0

amount = sum(fish)

print(amount)
