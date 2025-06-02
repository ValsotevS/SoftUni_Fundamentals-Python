char_index_start = int(input())
char_index_final = int(input())
final_characters = ""
for i in range(char_index_start, char_index_final + 1):
    character = chr(i)
    final_characters += character + " "

print(final_characters)