single_string = input()

numbers_list = single_string.split(" ")
opposite_numbers_as_integers = []

for current_number in numbers_list:
    current_number_as_integer = int(current_number)
    opposite_number = -current_number_as_integer
    opposite_numbers_as_integers.append(opposite_number)

print(opposite_numbers_as_integers)