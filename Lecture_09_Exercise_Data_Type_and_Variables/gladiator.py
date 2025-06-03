lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
broken_shield_counter = 0

for fight in range(1, lost_fights_count + 1):

    if fight % 2 == 0:
        total_expenses += helmet_price
        if fight % 3 == 0:
            broken_shield_counter += 1
            total_expenses += sword_price
            total_expenses += shield_price
            if broken_shield_counter % 2 == 0:
                total_expenses += armor_price
    elif fight % 3 == 0:
        total_expenses += sword_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")


