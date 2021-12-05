with open("input.txt") as f:
    data = f.read().splitlines()

coordinates = set()
double_coordinates = set()

for line in data:
    first_coordinate, second_coordinate = line.split(" -> ")

    first_coordinate = tuple(map(int, first_coordinate.split(",")))
    second_coordinate = tuple(map(int, second_coordinate.split(",")))

    if first_coordinate[0] == second_coordinate[0]:
        index = 1
    elif first_coordinate[1] == second_coordinate[1]:
        index = 0
    else:
        continue

    new_coordinates = [
        (first_coordinate[0], coordinate)
        if index == 1
        else (coordinate, second_coordinate[1])
        for coordinate in range(
            min(first_coordinate[index], second_coordinate[index]),
            max(first_coordinate[index], second_coordinate[index]) + 1,
        )
    ]

    for coordinate in new_coordinates:
        if coordinate in coordinates:
            double_coordinates.add(coordinate)

        coordinates.add(coordinate)

amount = len(double_coordinates)

print(amount)
