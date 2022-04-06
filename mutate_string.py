first_string = input()
second_string = input()

last_string = first_string

for i in range(len(second_string)):
    new_string = ''
    for beginning in range(0, i + 1):
        new_string += second_string[beginning]
    for ending in range(i + 1, len(first_string)):
        new_string += first_string[ending]
    if new_string == last_string:
        continue

    print(new_string)

    last_string = new_string

# first_string = input()
# second_string = input()
#
# last_string = first_string
#
# for i in range(len(second_string)):
#     left_part = second_string[:i + 1]
#     right_part = first_string[i + 1:]
#     current_string = left_part + right_part
#     if current_string == last_string:
#         continue
#
#     print(current_string)
#     last_string = current_string
