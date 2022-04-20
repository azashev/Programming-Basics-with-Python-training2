def string_to_int(x):
    new_list = []
    for i in x:
        new_list.append(int(i))
    return new_list


def filter_to_ints(digits):
    return digits % 2 == 0


numbers = input().split()
list_of_integers = string_to_int(numbers)

result = list(filter(filter_to_ints, list_of_integers))

print(result)
