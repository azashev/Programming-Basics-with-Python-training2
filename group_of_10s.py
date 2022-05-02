numbers = [int(x) for x in input().split(", ")]

counter = 0
group = 10

while counter < len(numbers):
    new_list = []
    for n in numbers:
        if group - 10 < n <= group:
            new_list.append(n)
            counter += 1
    print(f"Group of {group}'s: {new_list}")
    group += 10
