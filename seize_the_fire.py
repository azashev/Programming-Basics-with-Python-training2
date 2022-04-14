command = input().split("#")
available_water = int(input())

first_list = list(command)
total_fire_put_out = 0
total_effort = 0
cells = []

for i in first_list:
    second_list = i.split(" = ")
    current_ceil = int(second_list[1])
    if second_list[0] == 'High' and 81 <= current_ceil <= 125 and available_water >= current_ceil:
        available_water -= current_ceil
        total_fire_put_out += current_ceil
        total_effort += current_ceil * 0.25
        cells.append(current_ceil)
    elif second_list[0] == 'Medium' and 51 <= current_ceil <= 80 and available_water >= current_ceil:
        available_water -= current_ceil
        total_fire_put_out += current_ceil
        total_effort += current_ceil * 0.25
        cells.append(current_ceil)
    elif second_list[0] == 'Low' and 1 <= current_ceil <= 50 and available_water >= current_ceil:
        available_water -= current_ceil
        total_fire_put_out += current_ceil
        total_effort += current_ceil * 0.25
        cells.append(current_ceil)

print("Cells:")

for cell in cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")