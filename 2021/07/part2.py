with open("input.txt") as f:
    data = f.read().split(",")

positions = list(map(int, data))

minimum_fuel_cost = 10 ** 12

for position in range(max(positions)):
    difference = [
        int(
            (abs(current_position - position) / 2)
            * (abs(current_position - position) + 1)
        )
        for current_position in positions
    ]

    if (fuel_cost := sum(difference)) < minimum_fuel_cost:
        minimum_fuel_cost = fuel_cost

print(minimum_fuel_cost)
