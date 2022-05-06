collected_items = input().split(", ")

craft = False

while True:
    command = input()
    if command == 'Craft!':
        craft = True
        break
    else:
        command = command.split(" - ")

    if command[0] == 'Collect':
        if command[1] in collected_items:
            continue
        else:
            collected_items.append(command[1])
    elif command[0] == 'Drop':
        if command[1] in collected_items:
            collected_items.remove(command[1])
    elif command[0] == 'Combine Items':
        combine_command = [x for x in command[1].split(":")]
        old_item = combine_command[0]
        new_item = combine_command[1]
        if old_item in collected_items:
            index_old_item = collected_items.index(old_item)
            collected_items.insert(index_old_item + 1, new_item)
    elif command[0] == 'Renew':
        if command[1] in collected_items:
            collected_items.remove(command[1])
            collected_items.append(command[1])


if craft:
    print(', '.join(collected_items))
