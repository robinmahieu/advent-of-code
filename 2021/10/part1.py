with open("input.txt") as f:
    data = f.read().splitlines()

open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
distribution = {")": 3, "]": 57, "}": 1197, ">": 25137}

illegal_characters = list()

for line in data:
    to_close = list()

    for character in line:
        if character in open_close:
            to_close.append(open_close[character])
        else:
            if character == to_close[-1]:
                del to_close[-1]
            else:
                illegal_characters.append(character)
                break

points = 0

for character in illegal_characters:
    points += distribution[character]

print(points)
