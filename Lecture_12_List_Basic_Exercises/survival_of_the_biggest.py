list_of_integers = list(map(int, input().split(" ")))
how_many_numbers_to_remove = int(input())

for _ in range(how_many_numbers_to_remove):
    lowest_num = min(list_of_integers)
    list_of_integers.remove(lowest_num)

print(", ".join(str(num) for num in list_of_integers))
