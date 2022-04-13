card_deck = input().split()
shuffles = int(input())

result = []

for i in range(shuffles):
    result = []
    half_deck = len(card_deck) // 2
    left_part = card_deck[:half_deck]
    right_part = card_deck[half_deck::]

    for card in range(len(left_part)):
        result.append(left_part[card])
        result.append(right_part[card])

    card_deck = result
print(card_deck)