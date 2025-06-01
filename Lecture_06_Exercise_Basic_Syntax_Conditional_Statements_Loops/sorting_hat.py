new_student = str(input())

while new_student != "Welcome!":

    if new_student == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(new_student) < 5:
        print(f"{new_student} goes to Gryffindor.")
    elif len(new_student) == 5:
        print(f"{new_student} goes to Slytherin.")
    elif len(new_student) == 6:
        print(f"{new_student} goes to Ravenclaw.")
    elif len(new_student) > 6:
        print(f"{new_student} goes to Hufflepuff.")

    new_student = str(input())
    if new_student == "Welcome!":
        print("Welcome to Hogwarts.")
