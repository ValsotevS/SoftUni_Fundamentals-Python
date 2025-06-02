number_of_lines = int(input())
water_tank_capacity = 255
liters_poured = 0
for i in range(number_of_lines):
    liters = int(input())
    if liters_poured + liters > 255:
        print("Insufficient capacity!")
    else:
        liters_poured += liters

print(liters_poured)