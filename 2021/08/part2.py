with open("input.txt") as f:
    data = f.read().splitlines()

signals = [line.split(" | ")[0].split() for line in data]
output_values = [line.split(" | ")[1].split() for line in data]

counter = 0

for line, signal in enumerate(signals):
    mapping = [0] * 7  # top, lt, rt, mid, lb, rb, bot

    patterns = dict()

    lengths = dict()
    occurences = dict()

    for value in signal:
        lengths[len(value)] = value

        for character in value:
            if character in occurences:
                occurences[character] += 1
            else:
                occurences[character] = 1

    for character, amount in occurences.items():
        match amount:
            case 4:
                mapping[4] = character
            case 6:
                mapping[1] = character
            case 9:
                mapping[5] = character

    # determine rt
    one = list(lengths[2])

    patterns[frozenset(one)] = "1"

    one.remove(mapping[5])

    mapping[2] = one[0]

    # determine top
    seven = list(lengths[3])

    patterns[frozenset(seven)] = "7"

    for index in (2, 5):
        seven.remove(mapping[index])

    mapping[0] = seven[0]

    # determine mid
    four = list(lengths[4])

    patterns[frozenset(four)] = "4"

    for character in (1, 2, 5):
        four.remove(mapping[character])

    mapping[3] = four[0]

    # determine bot
    value = [character for character in "abcdefg" if character not in mapping]

    mapping[6] = value[0]

    combinations = [
        ["9", [4]],
        ["8", []],
        ["6", [2]],
        ["5", [2, 4]],
        ["3", [1, 4]],
        ["2", [1, 5]],
        ["0", [3]],
    ]

    for value, forbidden in combinations:
        patterns[
            frozenset(
                [
                    character
                    for index, character in enumerate(mapping)
                    if index not in forbidden
                ]
            )
        ] = value

    counter += int(
        "".join([patterns[frozenset(value)] for value in output_values[line]])
    )

print(counter)
