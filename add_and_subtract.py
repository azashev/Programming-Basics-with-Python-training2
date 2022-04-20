def sum_numbers(a, b):
    return a + b


def subtract(sum_first_two_numbers, num_three):
    return sum_first_two_numbers - num_three


def add_and_subtract(one, two, three):
    final_sum = sum_numbers(one, two)
    result = subtract(final_sum, three)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
