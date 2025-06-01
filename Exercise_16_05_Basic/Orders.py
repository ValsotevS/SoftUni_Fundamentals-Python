number_of_order = int(input())
total_price = 0
for order in range(number_of_order):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    current_day_price = (price_per_capsule * capsules_per_day) * days
    total_price += current_day_price
    print(f"The price for the coffee is: ${current_day_price:.2f}")

print(f"Total: ${total_price:.2f}")
