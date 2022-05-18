population = [int(x) for x in input().split(', ')]
min_wealth = int(input())

wealthiest_part = 0

for i in population:
    if i > wealthiest_part:
        wealthiest_part = i

for x in range(len(population) - 1):
    reduced_num = wealthiest_part - (min_wealth - population[x])
    if population[x] < min_wealth:
        if reduced_num >= min_wealth:
            for num in range(len(population)):
                if population[num] == wealthiest_part:
                    population[num] -= min_wealth - population[x]
                    wealthiest_part -= min_wealth - population[x]
            population[x] += min_wealth - population[x]
            for i in population:
                if i > wealthiest_part:
                    wealthiest_part = i

is_valid = True

for element in population:
    if element < min_wealth:
        is_valid = False

if is_valid:
    print(population)
else:
    print("No equal distribution possible")

