gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break

    current_command = command.split()
    current_gift = current_command[1]

    if current_command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == current_gift:
                gifts[i] = "None"
    elif current_command[0] == 'Required':
        current_index = int(current_command[2])
        if 0 <= int(current_command[2]) < len(gifts):
            gifts[current_index] = current_gift
    elif current_command[0] == 'JustInCase':
        gifts[-1] = current_gift

while 'None' in gifts:
    gifts.remove('None')

print(*gifts)