import statistics

with open("input.txt") as f:
    data = f.read().splitlines()

open_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
distribution = {")": 1, "]": 2, "}": 3, ">": 4}

scores = list()

for line in data:
    to_close = list()

    corrupted = False

    for character in line:
        if character in open_close:
            to_close.append(open_close[character])
        else:
            if character == to_close[-1]:
                del to_close[-1]
            else:
                corrupted = True
                break

    if corrupted or not to_close:
        continue

    score = 0

    for character in reversed(to_close):
        score *= 5
        score += distribution[character]

    scores.append(score)

middle_score = statistics.median(scores)

print(middle_score)
