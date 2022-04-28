number_of_rooms = int(input())
chairs = []
guests = 0

free_chairs = 0
passed = True

for room in range(1, number_of_rooms + 1):
    chairs = input().split()
    guests = chairs[1]
    chairs.pop()

    if len(chairs[0]) >= int(guests):
        free_chairs += len(chairs[0]) - int(guests)
    else:
        diff = int(guests) - len(chairs[0])
        passed = False
        print(f"{diff} more chairs needed in room {room}")

if passed:
    print(f"Game On, {free_chairs} free chairs left")
