def is_valid(element1, element2):
    return 0 <= element1 < len(elements) and 0 <= element2 < len(elements)


elements = input().split()

command = input()

moves_counter = 0

while command != "end":

    command = command.split()
    element_one = int(command[0])
    element_two = int(command[1])

    moves_counter += 1

    if not is_valid(element_one, element_two) or element_one == element_two:
        elements_middle_index = len(elements) // 2
        new_item = f"-{moves_counter}a"
        elements.insert(elements_middle_index, new_item)
        elements.insert(elements_middle_index, new_item)
        print("Invalid input! Adding additional elements to the board")

        moves_counter += 1
        command = input()
        continue

    if elements[element_one] == elements[element_two]:
        matching_element = elements[element_one]
        if element_one >= element_two:
            elements.pop(element_one)
            elements.pop(element_two)
        else:
            elements.pop(element_two)
            elements.pop(element_one)
        print(f"Congrats! You have found matching elements - {matching_element}!")
    elif elements[element_one] != elements[element_two]:
        print("Try again!")

    if len(elements) < 1:
        print(f"You have won in {moves_counter} turns!")
        break

    command = input()

if command == "end":
    if len(elements) > 0:
        print("Sorry you lose :(")
        print(' '.join(elements))
