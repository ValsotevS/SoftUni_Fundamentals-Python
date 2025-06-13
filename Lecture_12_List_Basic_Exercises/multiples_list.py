# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order,
# starting from the value of the factor.

my_list = []

factor = int(input())
count = int(input())

for num in range(1, count + 1):
    current_number = num
    my_list.append(current_number * factor)

print(my_list)