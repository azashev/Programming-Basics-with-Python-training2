def perfect_num(num):
    sum = 0
    for i in range(1, int(num)):
        if int(num) % int(i) == 0:
            sum += int(i)
    if sum == int(num):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


text = input()

perfect_num(text)
