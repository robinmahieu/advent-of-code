with open("input.txt") as f:
    data = f.read().splitlines()


def calculate_rating(data, most_common=True):
    for index in range(len(data[0])):
        if all([row[index] == data[0][index] for row in data]):
            continue

        bits = [row[index] for row in data]

        zeros, ones = bits.count("0"), bits.count("1")

        if most_common:
            bit_criterium = "0" if zeros > ones else "1"
        else:
            bit_criterium = "1" if ones < zeros else "0"

        for row in data[:]:
            if row[index] != bit_criterium:
                data.remove(row)

        if len(data) == 1:
            return data[0]

    return "no solution found"


oxygen_generator_data, co2_scrubber_data = data[:], data[:]

oxygen_generator_rating = calculate_rating(oxygen_generator_data)
co2_scrubber_rating = calculate_rating(co2_scrubber_data, False)

product = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)

print(product)
