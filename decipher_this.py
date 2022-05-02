from curses.ascii import isdigit

secret_message = [x for x in input().split()]
message = ''

for word in secret_message:
    numbers = ''
    for ch in word:
        if isdigit(ch):
            numbers += ch
    word = word.replace(numbers, chr(int(numbers)))
    word_list = list(word)

    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    word = ''.join(word_list)
    print(word, end=' ')
