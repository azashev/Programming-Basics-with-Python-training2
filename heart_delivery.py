neighborhood = [int(x) for x in input().split("@")]

current_command = ''
position = 0

while True:
    command = input()
    if command == "Love!":
        break
    else:
        command = list(command.split())

    if int(command[1]) + position > len(neighborhood) - 1:
        position = 0
    else:
        position += int(command[1])

    neighborhood[position] -= 2

    if neighborhood[position] == 0:
        print(f"Place {position} has Valentine's day.")

    elif neighborhood[position] < 2:
        print(f"Place {position} already had Valentine's day.")

    last_position = position

print(f"Cupid's last position was {position}.")

failed_places = [x for x in neighborhood if x > 0]

if failed_places:
    print(f"Cupid has failed {len(failed_places)} places.")
else:
    print("Mission was successful.")
