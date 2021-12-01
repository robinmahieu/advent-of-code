with open("input.txt") as f:
    data = f.read().splitlines()

increases = 0

for first_depth, second_depth in zip(data, data[1:]):
    if int(first_depth) < int(second_depth):
        increases += 1

print(increases)
