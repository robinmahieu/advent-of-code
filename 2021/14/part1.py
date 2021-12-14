with open("input.txt") as f:
    data = f.read()

template, instructions = data.split("\n\n")

instructions = dict(
    (instruction.split(" -> ") for instruction in instructions.splitlines())
)

for _ in range(10):
    new_template = str()

    for elements in zip(template, template[1:]):
        new_element = instructions[elements[0] + elements[1]]

        new_template += elements[0] + new_element

    template = new_template + template[-1]

counts = {template.count(unique_element) for unique_element in set(template)}

difference = max(counts) - min(counts)

print(difference)
