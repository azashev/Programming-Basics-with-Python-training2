number = int(input())

for i in range(number):
    sum = ''
    for s in range(number):
        for l in range(number):
            #sum += chr(97 + l)
            sum = chr(97 + i) + chr(97 + s) + chr(97 + l)
            print(sum)
