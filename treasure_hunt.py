from audioop import reverse


def is_valid(index):
    return 0 <= index < len(items)


items = [item for item in input().split("|")]

command = input().split()

while command[0] != "Yohoho!":
    if command[0] == "Loot":
        loot_items = command[1::]
        for item in loot_items:
            if item not in items:
                items.insert(0, item)
            else:
                continue
    elif command[0] == "Drop":
        drop_index = int(command[1])
        if is_valid(drop_index):
            dropped_item = items.pop(drop_index)
            items.append(dropped_item)
        else:
            command = input().split()
            continue
    elif command[0] == "Steal":
        items_to_steal = int(command[1])
        stolen_items = []
        if items_to_steal >= len(items):
            stolen_items = items
            print(', '.join(stolen_items))
            items.clear()
        else:
            for i in range(items_to_steal):
                popped_item = items.pop()
                stolen_items.append(popped_item)

            stolen_items.reverse()
            print(', '.join(stolen_items))
    command = input().split()


if len(items) > 0:
    sum_treasure_items = 0
    for item in items:
        for ch in item:
            sum_treasure_items += 1
    average_treasure_gain = sum_treasure_items / len(items)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
