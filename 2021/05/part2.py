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
        index = -1

    if index in (0, 1):
        new_coordinates = [
            (first_coordinate[0], coordinate)
            if index == 1
            else (coordinate, second_coordinate[1])
            for coordinate in range(
                min(first_coordinate[index], second_coordinate[index]),
                max(first_coordinate[index], second_coordinate[index]) + 1,
            )
        ]
    else:
        translation = (
            1 if second_coordinate[0] > first_coordinate[0] else -1,
            1 if second_coordinate[1] > first_coordinate[1] else -1,
        )

        new_coordinates = [first_coordinate]

        while first_coordinate != second_coordinate:
            first_coordinate = (
                first_coordinate[0] + translation[0],
                first_coordinate[1] + translation[1],
            )

            new_coordinates.append(first_coordinate)

    for coordinate in new_coordinates:
        if coordinate in coordinates:
            double_coordinates.add(coordinate)

        coordinates.add(coordinate)

amount = len(double_coordinates)

print(amount)
