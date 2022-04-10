lines = int(input())

capacity = 255
poured_water = 0

for i in range(lines):
    liters_of_water = int(input())
    if poured_water + liters_of_water <= capacity:
        poured_water += liters_of_water
    else:
        print("Insufficient capacity!")
        continue

print(poured_water)
