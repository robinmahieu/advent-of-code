with open("input.txt") as f:
    data = f.read().splitlines()

gamma_rate, epsilon_rate = str(), str()

for index in range(len(data[0])):
    bits = [row[index] for row in data]

    zeros, ones = bits.count("0"), bits.count("1")

    gamma_rate += "0" if zeros > ones else "1"
    epsilon_rate += "1" if zeros > ones else "0"

product = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(product)
