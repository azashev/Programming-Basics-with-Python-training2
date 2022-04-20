def odd_and_even(num):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for i in num:
        if int(i) % 2 == 0:
            sum_of_even_digits += int(i)
        else:
            sum_of_odd_digits += int(i)

    return sum_of_odd_digits, sum_of_even_digits


number = list(input())

odd_digits_sum, even_digits_sum = odd_and_even(number)

print(f"Odd sum = {odd_digits_sum}, Even sum = {even_digits_sum}")
