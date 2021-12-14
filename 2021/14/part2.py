from math import ceil

with open("input.txt") as f:
    data = f.read()

template, instructions = data.split("\n\n")

instructions = dict(
    (instruction.split(" -> ") for instruction in instructions.splitlines())
)

elements = dict()

for first_element, second_element in zip(template, template[1:]):
    if first_element + second_element in elements:
        elements[first_element + second_element] += 1
    else:
        elements[first_element + second_element] = 1

for _ in range(40):
    new_elements = elements.copy()

    for element, amount in elements.items():
        middle_element = instructions[element]

        created_elements = (
            element[0] + middle_element,
            middle_element + element[1],
        )

        for created_element in created_elements:
            if created_element in new_elements:
                new_elements[created_element] += amount
            else:
                new_elements[created_element] = amount

        new_elements[element] -= amount

    elements = new_elements

occurences = dict()

for combination, amount in elements.items():
    for element in combination:
        if element in occurences:
            occurences[element] += amount
        else:
            occurences[element] = amount

difference = ceil(max(occurences.values()) / 2) - ceil(
    (min(occurences.values())) / 2
)

if template[0] == template[-1] and occurences[template[0]] == min(
    occurences.values()
):
    difference -= 1

print(difference)
