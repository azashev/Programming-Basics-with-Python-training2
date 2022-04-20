def sort(digits):
    return sorted(digits)


numbers = input().split()
numbers_int = []

for number in numbers:
    numbers_int.append(int(number))

sorted_numbers = list(sort(numbers_int))

print(sorted_numbers)
