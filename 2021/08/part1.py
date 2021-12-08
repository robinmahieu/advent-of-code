with open("input.txt") as f:
    data = f.read().splitlines()

data = [line.split(" | ")[1].split() for line in data]

counter = 0

for output_values in data:
    for value in output_values:
        if len(value) in (2, 3, 4, 7):
            counter += 1

print(counter)
