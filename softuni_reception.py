first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())

total_efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

students = int(input())

hours_counter = 0

while students > 0:
    hours_counter += 1
    if hours_counter % 4 != 0:
        students -= total_efficiency_per_hour
    else:
        continue

print(f"Time needed: {hours_counter}h.")
