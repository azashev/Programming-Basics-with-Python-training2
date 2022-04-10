index_start = int(input())
index_last = int(input())

chars = ''

for i in range(index_start, index_last + 1):
    chars = chr(i)
    print(chars + ' ', end='')