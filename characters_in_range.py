def chars_range(char_one, char_two):
    chars_in_range = []
    for i in range(ord(char_one) + 1, ord(char_two)):
        chars_in_range.append(chr(i))
    return chars_in_range


first_char = input()
second_char = input()

result = chars_range(first_char, second_char)

print(' '.join(result))
