quantity = int(input())
days = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_light = 15

cost = 0
spirit = 0

for days_left in range(1, days + 1):

    if days_left % 11 == 0:
        quantity += 2

    if days_left % 2 == 0:
        cost += price_ornament_set * quantity
        spirit += 5
    if days_left % 3 == 0:
        cost += (price_tree_skirt + price_tree_garlands) * quantity
        spirit += 13
    if days_left % 5 == 0:
        cost += price_tree_light * quantity
        spirit += 17
        if days_left % 3 == 0:
            spirit += 30
    if days_left % 10 == 0:
        spirit -= 20
        cost += price_tree_skirt + price_tree_garlands + price_tree_light

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")
