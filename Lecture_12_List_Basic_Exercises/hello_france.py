MAX_PRICE_CLOTHES = 50.00
MAX_PRICE_SHOES = 35.00
MAX_PRICE_ACCESSORIES = 20.50
PRICE_INCREASE = 0.4
TICKET_TO_FRANCE = 150

list_of_bought_items_price = []

collection_of_items = input().split("|")
starting_budget = float(input())
remaining_budget = starting_budget
total_spent = 0

for item in collection_of_items:
    item_info = item.split("->")
    type_of_item = item_info[0]
    price_of_item = float(item_info[1])

    if type_of_item == "Clothes":
        if price_of_item > MAX_PRICE_CLOTHES:
            continue
        if price_of_item <= remaining_budget:
            remaining_budget -= price_of_item
            total_spent += price_of_item
            price_of_item = price_of_item + (price_of_item * PRICE_INCREASE)
            list_of_bought_items_price.append(price_of_item)

        else:
            continue
    elif type_of_item == "Shoes":
        if price_of_item > MAX_PRICE_SHOES:
            continue
        if price_of_item <= remaining_budget:
            remaining_budget -= price_of_item
            total_spent += price_of_item
            price_of_item = price_of_item + (price_of_item * PRICE_INCREASE)
            list_of_bought_items_price.append(price_of_item)

        else:
            continue
    elif type_of_item == "Accessories":
        if price_of_item > MAX_PRICE_ACCESSORIES:
            continue
        if price_of_item <= remaining_budget:
            total_spent += price_of_item
            remaining_budget -= price_of_item
            price_of_item = price_of_item + (price_of_item * PRICE_INCREASE)
            list_of_bought_items_price.append(price_of_item)

        else:
            continue

total_new_price = sum(list_of_bought_items_price)
profit = total_new_price - total_spent

total_money = starting_budget + profit

print(" ".join([f"{price:.2f}" for price in list_of_bought_items_price]))
print(f"Profit: {profit:.2f}")

if total_money >= TICKET_TO_FRANCE:
    print("Hello, France!")
else:
    print("Not enough money.")
