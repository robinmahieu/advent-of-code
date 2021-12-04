class Board:
    def __init__(self, rows):
        self.rows = rows

        self.found_numbers = list()

    def draw_number(self, number):
        for row_index, row in enumerate(self.rows):
            if number not in row:
                continue

            column_index = row.index(number)
            self.found_numbers.append((row_index, column_index))

            return self.has_bingo

    @property
    def has_bingo(self):
        row_indexes, column_indexes = list(), list()

        for row_index, column_index in self.found_numbers:
            row_indexes.append(row_index)
            column_indexes.append(column_index)

            if (
                row_indexes.count(row_index) == 5
                or column_indexes.count(column_index) == 5
            ):
                return True

        return False

    @property
    def unmarked_numbers(self):
        numbers = list()

        for row_index, row in enumerate(self.rows):
            for column_index, number in enumerate(row):
                if not (row_index, column_index) in self.found_numbers:
                    numbers.append(int(number))

        return numbers
