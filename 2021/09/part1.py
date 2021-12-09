with open("input.txt") as f:
    data = f.read().splitlines()

translations = {(1, 0), (-1, 0), (0, 1), (0, -1)}

row_range, column_range = range(len(data)), range(len(data[0]))

counter = 0

for row_index, row in enumerate(data):
    for column_index, column in enumerate(row):
        neighbours = {
            int(data[row_index + y_translation][column_index + x_translation])
            for x_translation, y_translation in translations
            if column_index + x_translation in column_range
            and row_index + y_translation in row_range
        }

        column = int(column)

        is_lowest = all({column < neighbour for neighbour in neighbours})

        if is_lowest:
            counter += column + 1

print(counter)
