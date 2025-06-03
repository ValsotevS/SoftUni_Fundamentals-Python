char_index_start = int(input())
char_index_final = int(input())

for i in range(char_index_start, char_index_final + 1):
    character = chr(i)
    if i == char_index_final:
        print(character)
    else:
        print(character, end= " ")
