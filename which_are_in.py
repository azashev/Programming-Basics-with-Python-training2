first_line = input().split(", ")
second_line = input().split(", ")

new_list = []

for i in first_line:
    for s in second_line:
        if i in s and i not in new_list:
            new_list.append(i)

print(new_list)
