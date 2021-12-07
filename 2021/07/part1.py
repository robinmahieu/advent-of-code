with open("input.txt") as f:
    data = f.read().split(",")

positions = list(map(int, data))

minimum_fuel_cost = 10 ** 12

for position in range(max(positions)):
    difference = [
        abs(current_position - position) for current_position in positions
    ]

    if (fuel_cost := sum(difference)) < minimum_fuel_cost:
        minimum_fuel_cost = fuel_cost

print(minimum_fuel_cost)
