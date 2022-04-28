number_of_electrons = int(input())

distributed_electrons = []

counter = 1

while number_of_electrons > 0:
    if number_of_electrons - (2 * counter**2) >= 0:
        distributed_electrons.append(2 * counter**2)
        number_of_electrons -= 2 * counter**2
        counter += 1
    else:
        distributed_electrons.append(number_of_electrons)
        break

print([int(x) for x in distributed_electrons])
