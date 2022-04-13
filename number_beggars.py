numbers = input().split(", ")
beggars = int(input())

result = []

for num in range(beggars):
    current_result = 0
    for sum in range(num, len(numbers), beggars):
        current_result += int(numbers[sum])
    result.append(current_result)

print(result)