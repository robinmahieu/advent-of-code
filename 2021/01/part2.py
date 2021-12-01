with open("input.txt") as f:
    data = f.read().splitlines()

depth_sums = [
    sum((int(first_depth), int(second_depth), int(third_depth)))
    for first_depth, second_depth, third_depth in zip(
        data, data[1:], data[2:]
    )
]

increases = 0

for first_depth_sum, second_depth_sum in zip(depth_sums, depth_sums[1:]):
    if first_depth_sum < second_depth_sum:
        increases += 1

print(increases)
