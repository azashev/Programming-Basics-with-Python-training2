def loading_bar(num):
    if num == 100:
        print(f"100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{num}% [{'%' * (num // 10)}{'.' * (10 - (num // 10))}]\n Still loading...")


int_number = int(input())

loading_bar(int_number)
