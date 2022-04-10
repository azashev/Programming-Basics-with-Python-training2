lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_brakes = 0
expenses = 0

for fight in range(1, lost_fights + 1):
    helmet_broken = False
    sword_broken = False
    if fight % 2 == 0:
        expenses += helmet_price
        helmet_broken = True
    if fight % 3 == 0:
        expenses += sword_price
        sword_broken = True
    if helmet_broken and sword_broken:
        expenses += shield_price
        shield_brakes += 1
    if shield_brakes != 0 and shield_brakes % 2 == 0:
        expenses += armor_price
        shield_brakes = 0

print(f"Gladiator expenses: {expenses:.1f} aureus")