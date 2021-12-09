from math import prod

with open("input.txt") as f:
    data = f.read().splitlines()

translations = ((1, 0), (-1, 0), (0, 1), (0, -1))

row_range, column_range = range(len(data)), range(len(data[0]))

low_points = set()

for row_index, row in enumerate(data):
    for column_index, column in enumerate(row):
        neighbours = {
            (column_index + x_translation, row_index + y_translation)
            for x_translation, y_translation in translations
            if column_index + x_translation in column_range
            and row_index + y_translation in row_range
        }

        is_lowest = all(
            {
                int(column) < int(data[y_coordinate][x_coordinate])
                for x_coordinate, y_coordinate in neighbours
            }
        )

        if is_lowest:
            low_points.add((column_index, row_index))


def add_neighbour_points(x_coordinate, y_coordinate):
    neighbours = [
        (x_coordinate + x_translation, y_coordinate + y_translation)
        for x_translation, y_translation in translations
        if x_coordinate + x_translation in column_range
        and y_coordinate + y_translation in row_range
    ]

    for x_coordinate, y_coordinate in neighbours:
        if (
            not (x_coordinate, y_coordinate) in basin
            and data[y_coordinate][x_coordinate] != "9"
        ):
            basin.add((x_coordinate, y_coordinate))

            add_neighbour_points(x_coordinate, y_coordinate)


largest_basins = [0] * 3

for x_coordinate, y_coordinate in low_points:
    basin = set()

    add_neighbour_points(x_coordinate, y_coordinate)

    if len(basin) > (smallest := min(largest_basins)):
        largest_basins.remove(smallest)
        largest_basins.append(len(basin))

product = prod(largest_basins)

print(product)
