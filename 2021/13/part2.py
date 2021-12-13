with open("input.txt") as f:
    data = f.read()

coordinate_data, fold_data = data.split("\n\n")

coordinates = {
    (int(x_coordinate), int(y_coordinate))
    for x_coordinate, y_coordinate in (
        coordinate.split(",") for coordinate in coordinate_data.splitlines()
    )
}

folds = (
    (direction[-1], int(value))
    for direction, value in (
        fold.split("=") for fold in fold_data.splitlines()
    )
)

for direction, value in folds:
    if direction == "x":
        for x_coordinate, y_coordinate in coordinates.copy():
            if x_coordinate > value:
                new_x_coordinate = 2 * value - x_coordinate

                coordinates.remove((x_coordinate, y_coordinate))
                coordinates.add((new_x_coordinate, y_coordinate))
    else:
        for x_coordinate, y_coordinate in coordinates.copy():
            if y_coordinate > value:
                new_y_coordinate = 2 * value - y_coordinate

                coordinates.remove((x_coordinate, y_coordinate))
                coordinates.add((x_coordinate, new_y_coordinate))

max_x_coordinate = max({x_coordinate for x_coordinate, _ in coordinates})
max_y_coordinate = max({y_coordinate for _, y_coordinate in coordinates})

grid = [["."] * (max_x_coordinate + 1) for _ in range(max_y_coordinate + 1)]

for x_coordinate, y_coordinate in coordinates:
    grid[y_coordinate][x_coordinate] = "#"

for line in grid:
    print("".join(line))
