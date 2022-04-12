energy = 100
coins = 100

events = input().split("|")

cannot_afford = False

for event in events:
    current_events = event.split("-")
    current_event = current_events[0]
    current_value = int(current_events[1])

    if current_event == 'rest':
        if energy + current_value <= 100:
            energy += current_value
            print(f"You gained {current_value} energy.")
        else:
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")
    elif current_event == 'order':
        if energy - 30 >= 0:
            energy -= 30
            coins += current_value
            print(f"You earned {current_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - current_value >= 0:
            coins -= current_value
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            cannot_afford = True
            break

if not cannot_afford:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")