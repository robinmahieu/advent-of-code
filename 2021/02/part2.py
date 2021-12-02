with open("input.txt") as f:
    data = f.read().splitlines()

horizontal, vertical, aim = 0, 0, 0

for command in data:
    direction, amount = command.split()

    match direction:
        case "forward":
            horizontal += int(amount)
            vertical += int(amount) * aim
        case "down":
            aim += int(amount)
        case "up":
            aim -= int(amount)

product = horizontal * vertical

print(product)
