numbers = input().split()
numbers_to_remove = int(input())

list_of_numbers = list(numbers)

for i in range(len(numbers)):
    list_of_numbers[i] = int(numbers[i])

for final in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

print(*list_of_numbers, sep=', ')