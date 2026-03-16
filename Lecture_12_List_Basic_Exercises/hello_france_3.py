list_of_items = input().split("|")
budget = float(input())
total_spent = 0

bought_items_new_price_lst = []

ticket_to_france_coast = 150

for item in list_of_items:
    new_item = item.split("->")
    current_item = new_item[0]
    current_item_value = float(new_item[1])

    if current_item_value > budget:
        continue

    elif current_item == "Clothes" and current_item_value <= 50.00:
        budget -= current_item_value
        current_item_new_value = current_item_value + (current_item_value * 0.40)
        total_spent += current_item_value
        bought_items_new_price_lst.append(current_item_new_value)

    elif current_item == "Shoes" and current_item_value <= 35.00:
        budget -= current_item_value
        current_item_new_value = current_item_value + (current_item_value * 0.40)
        total_spent += current_item_value
        bought_items_new_price_lst.append(current_item_new_value)

    elif current_item == "Accessories" and current_item_value <= 20.50:
        budget -= current_item_value
        current_item_new_value = (current_item_value + (current_item_value * 0.40))
        total_spent += current_item_value
        bought_items_new_price_lst.append(current_item_new_value)

profit = sum(bought_items_new_price_lst) - total_spent
money_available = budget + sum(bought_items_new_price_lst)

print(" ".join([f"{price:.2f}" for price in bought_items_new_price_lst]))
print(f"Profit: {profit:.2f}")

if money_available >= ticket_to_france_coast:
    print("Hello, France!")
else:
    print("Not enough money.")
