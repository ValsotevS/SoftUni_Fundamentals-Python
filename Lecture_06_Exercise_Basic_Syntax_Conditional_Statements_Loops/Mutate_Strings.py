first_string = str(input())
second_string = str(input())
last_printed_string = first_string
for char_index in range(len(first_string)):
    left_part = second_string[:char_index + 1]
    right_part = first_string[char_index + 1:]
    new_string = left_part + right_part
    if new_string != last_printed_string:
        print(new_string)
        last_printed_string = new_string