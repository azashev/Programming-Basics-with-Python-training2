def length_checker(txt):
    if 6 <= len(txt) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")


def letters_digits_checker(txt):
    if txt.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")


def digits_checker(txt):
    digit_counter = 0
    for i in txt:
        if i.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    else:
        print("Password must have at least 2 digits")


password = input()

check_length = length_checker(password)
check_letters_digits = letters_digits_checker(password)
check_digits = digits_checker(password)

if check_length and check_letters_digits and check_digits:
    print("Password is valid")
