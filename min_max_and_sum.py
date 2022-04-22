def min_number(n):
    print(f"The minimum number is {min(n)}")
    print(f"The maximum number is {max(n)}")
    print(f"The sum number is: {sum(n)}")


given_numbers_list = input().split()
given_numbers_int = []

for i in given_numbers_list:
    given_numbers_int.append(int(i))

min_number(given_numbers_int)
