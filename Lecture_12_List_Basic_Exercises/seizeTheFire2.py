fire_cells = [cell for cell in input().split("#")]
water = int(input())

cells_putted_out = []
total_effort = 0

for cell in fire_cells:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell_value = int(current_cell[1])

    if type_of_fire == "High" and 81 <= cell_value <= 125:

        if cell_value > water:
            continue
        else:
            water -= cell_value
            cells_putted_out.append(cell_value)
            total_effort += cell_value * 0.25
    elif type_of_fire == "Medium" and 51 <= cell_value <= 80:

        if cell_value > water:
            continue
        else:
            water -= cell_value
            cells_putted_out.append(cell_value)
            total_effort += cell_value * 0.25

    elif type_of_fire == "Low" and 1 <= cell_value <= 50:

        if cell_value > water:
            continue
        else:
            water -= cell_value
            cells_putted_out.append(cell_value)
            total_effort += cell_value * 0.25

print(f"Cells:")
for cell in cells_putted_out:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(int(num) for num in cells_putted_out)}")