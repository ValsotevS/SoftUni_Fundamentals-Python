"""On the first line, you will receive a number n.
On the following n lines, you will receive integers. You should create and print two lists:
· One with all the positive (including 0) numbers
· One with all the negative numbers

Finally, print the following message:
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"""

positive_numbers_list = []
negative_numbers_list = []

number_of_lines = int(input())

for _ in range(number_of_lines):
    current_number = int(input())
    if current_number < 0:
        negative_numbers_list.append(current_number)
    else:
        positive_numbers_list.append(current_number)

count_positive_numbers = len(positive_numbers_list)
sum_negative_numbers = sum(negative_numbers_list)

print(positive_numbers_list)
print(negative_numbers_list)

print(f"Count of positives: {count_positive_numbers}")
print(f"Sum of negatives: {sum_negative_numbers}")
