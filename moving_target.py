targets = [int(x) for x in input().split()]

while True:
    command = input()
    if command == 'End':
        print('|'.join(str(target) for target in targets))
        break
    else:
        command = command.split()
        current_index = int(command[1])
        current_value = int(command[2])

    if command[0] == 'Shoot':
        if 0 <= current_index < len(targets):
            targets[current_index] -= current_value
            if targets[current_index] <= 0:
                targets.pop(current_index)
    elif command[0] == 'Add':
        if 0 <= current_index < len(targets):
            targets.insert(current_index, current_value)
        else:
            print("Invalid placement!")
    elif command[0] == 'Strike':
        if 0 <= current_index < len(targets):
            if 0 <= current_index - current_value < len(targets) and current_index + current_value <= len(targets) + 1:
                targets = targets[:current_index - current_value] + targets[(current_index + current_value + 1):]
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")
