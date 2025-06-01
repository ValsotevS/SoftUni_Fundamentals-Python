number_of_messages = int(input())

for i in range(number_of_messages):
    code = int(input())
    current_message = ""
    if code == 88:
        current_message = "Hello"
    elif code == 86:
        current_message = "How are you?"
    elif code < 88:
        current_message = "GREAT!"
    else:
        current_message = "Bye."

    print(current_message)

