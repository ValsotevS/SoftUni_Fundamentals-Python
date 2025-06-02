number = int(input())
for current_number in range(1, number + 1):
    current_number_str = str(current_number)
    digits_sum = 0
    for current_digit in current_number_str:
        digits_sum += int(current_digit)

    is_Special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_Special = True

    print(f"{current_number} -> {is_Special}")