number_of_orders = int(input())

total_price = 0

for n in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    current_price = (days * capsules_count) * price_per_capsule
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")