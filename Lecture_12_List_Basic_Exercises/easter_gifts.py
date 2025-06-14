list_of_gifts = input().split(" ")
command = input()

while command != "No Money":

    current_command = command.split(" ")

    if current_command[0] == "OutOfStock":
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == current_command[1]:
                list_of_gifts[i] = "None"

    elif current_command[0] == "Required":
        if 0 <= int(current_command[2]) < len(list_of_gifts):
            current_index = int(current_command[2])
            list_of_gifts[current_index] = current_command[1]

    elif current_command[0] == "JustInCase":
        list_of_gifts[-1] = current_command[1]

    command = input()

for gift in list_of_gifts:
    if gift == "None":
        continue
    else:
        print(gift, end=" ")

