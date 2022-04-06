budget = float(input())
price_per_kg_flour = float(input())

current_bread_count = 0
colored_eggs = 0

price_eggs = price_per_kg_flour * 0.75
price_milk = price_per_kg_flour + (price_per_kg_flour * 0.25)
needed_milk = price_milk * 0.25

recipe = price_eggs + price_per_kg_flour + needed_milk

while True:
    if budget >= recipe:
        budget -= recipe
        current_bread_count += 1
        colored_eggs += 3
        if current_bread_count % 3 == 0:
            colored_eggs -= current_bread_count - 2
    else:
        break

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
