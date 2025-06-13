string_of_integers = input().split(", ")
count_of_beggars = int(input())

list_of_integers = [int(num) for num in string_of_integers]

final_list = []
start_index = 0

for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for i in range(start_index, len(list_of_integers), count_of_beggars):
        current_beggar_sum += list_of_integers[i]

    final_list.append(current_beggar_sum)
    start_index += 1

print(final_list)