RATE_OF_EFFORT = 0.25


fires = input().split("#")
water = int(input())

total_fire = 0
total_effort = 0
cells_put_out_list = []

for fire in fires:
    current_fire = fire.split(" = ")
    type_of_fire = current_fire[0]
    value_of_cell = int(current_fire[1])

    if water < value_of_cell:
        continue

    if type_of_fire == "High" and 81 <= value_of_cell <= 125:
        water -= value_of_cell
        total_fire += value_of_cell
        current_effort = value_of_cell * RATE_OF_EFFORT
        total_effort += current_effort
        cells_put_out_list.append(value_of_cell)

    elif type_of_fire == "Medium" and  51 <= value_of_cell <= 80:
        water -= value_of_cell
        total_fire += value_of_cell
        current_effort = value_of_cell * RATE_OF_EFFORT
        total_effort += current_effort
        cells_put_out_list.append(value_of_cell)

    elif type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        water -= value_of_cell
        total_fire += value_of_cell
        current_effort = value_of_cell * RATE_OF_EFFORT
        total_effort += current_effort
        cells_put_out_list.append(value_of_cell)

print("Cells:")
for cell in cells_put_out_list:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
