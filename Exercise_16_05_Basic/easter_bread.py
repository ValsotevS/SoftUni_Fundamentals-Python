budget = float(input())
flour_kg_price = float(input())
milk_l_price = flour_kg_price + (flour_kg_price * 0.25)
eggs_pack_price = flour_kg_price * 0.75

total_colored_eggs = 0
loaves_count = 0

price_per_loaf = flour_kg_price + eggs_pack_price + (milk_l_price / 4)

while budget > price_per_loaf:
    loaves_count += 1
    total_colored_eggs += 3
    budget -= price_per_loaf

    if loaves_count % 3 == 0:
        total_colored_eggs -= loaves_count - 2

print(f"You made {loaves_count} loaves of Easter bread! Now you have {total_colored_eggs} "
      f"eggs and {budget:.2f}BGN left.")
