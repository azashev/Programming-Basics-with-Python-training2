items = input().split("|")
budget = float(input())

products = list(items)
prices_bought_items = []
profit = 0

for product in products:
    current_product = product.split("->")
    price_current_product = float(current_product[1])
    if current_product[0] == 'Clothes' and price_current_product <= 50 and price_current_product <= budget:
        budget -= price_current_product
        prices_bought_items.append(price_current_product)
    elif current_product[0] == 'Shoes' and price_current_product <= 35 and price_current_product <= budget:
        budget -= price_current_product
        prices_bought_items.append(price_current_product)
    elif current_product[0] == 'Accessories' and price_current_product <= 20.50 and price_current_product <= budget:
        budget -= price_current_product
        prices_bought_items.append(price_current_product)

new_prices_bought_items = list(prices_bought_items)

for i in range(len(new_prices_bought_items)):
    profit += new_prices_bought_items[i] * 0.4
    new_prices_bought_items[i] = new_prices_bought_items[i] + (new_prices_bought_items[i] * 0.4)
    budget += new_prices_bought_items[i]
    print(f"{new_prices_bought_items[i]:.2f}", end=' ')

print()
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")