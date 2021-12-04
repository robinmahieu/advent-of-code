import sys

from board import Board

with open("input.txt") as f:
    data = f.read().splitlines()
    data.append("")

numbers = data.pop(0)
boards = list()

current_board = list()

for row in data[1:]:
    if row:
        current_board.append([number.strip() for number in row.split()])
    else:
        boards.append(Board(current_board))
        current_board = list()


for number in numbers.split(","):
    for board in boards:
        has_bingo = board.draw_number(number)

        if has_bingo:
            unmarked_numbers = board.unmarked_numbers
            product = sum(unmarked_numbers) * int(number)

            print(product)

            sys.exit()
