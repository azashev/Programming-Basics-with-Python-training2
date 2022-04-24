def factorial(num_one, num_two):
    first_factorial = num_one
    second_factorial = num_two

    for f in range(1, num_one):
        first_factorial *= f
    for s in range(1, num_two):
        second_factorial *= s
    return first_factorial, second_factorial


def result(number1, number2):
    first_result, second_result = factorial(number1, number2)
    final_result = first_result / second_result
    return final_result


first_num = int(input())
second_num = int(input())

print(f"{result(first_num, second_num):.2f}")
