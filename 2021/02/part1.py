with open("input.txt") as f:
    data = f.read().splitlines()

horizontal, vertical = 0, 0

for command in data:
    direction, amount = command.split()

    match direction:
        case "forward":
            horizontal += int(amount)
        case "down":
            vertical += int(amount)
        case "up":
            vertical -= int(amount)

product = horizontal * vertical

print(product)
