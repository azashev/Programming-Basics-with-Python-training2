def list_positives(numbers):
    return [str(x) for x in list_numbers if x >= 0]


def list_negatives(numbers):
    return [str(x) for x in list_numbers if x <= 0]


def list_evens(numbers):
    return [str(x) for x in list_numbers if x % 2 == 0]


def list_odds(numbers):
    return [str(x) for x in list_numbers if x % 2 != 0]


list_numbers = [int(x) for x in input().split(", ")]


print(f"Positive: {', '.join(list_positives(list_numbers))}")
print(f"Negative: {', '.join(list_negatives(list_numbers))}")
print(f"Even: {', '.join(list_evens(list_numbers))}")
print(f"Odd: {', '.join(list_odds(list_numbers))}")
