with open("input.txt") as f:
    data = f.read().splitlines()

data = [[int(column) for column in line] for line in data]

translations = {
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
}

column_range, row_range = range(10), range(10)

to_reset, counter = set(), 0


def flash(x_coordinate, y_coordinate):
    neighbours = {
        (x_coordinate + x_translation, y_coordinate + y_translation)
        for x_translation, y_translation in translations
        if x_coordinate + x_translation in column_range
        and y_coordinate + y_translation in row_range
    }

    for x_coordinate, y_coordinate in neighbours:
        data[y_coordinate][x_coordinate] += 1

        if data[y_coordinate][x_coordinate] == 10:
            to_reset.add((x_coordinate, y_coordinate))

            flash(x_coordinate, y_coordinate)


all_flashed = False

while not all_flashed:
    counter += 1

    for y_index, line in enumerate(data):
        for x_index in range(len(line)):
            data[y_index][x_index] += 1

            if data[y_index][x_index] == 10:
                to_reset.add((x_index, y_index))

                flash(x_index, y_index)

    if len(to_reset) == len(data) * len(data[0]):
        all_flashed = True

    for x_coordinate, y_coordinate in to_reset:
        data[y_coordinate][x_coordinate] = 0

    to_reset.clear()

print(counter)
