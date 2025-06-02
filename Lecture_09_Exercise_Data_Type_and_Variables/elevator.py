number_of_people = int(input())
elevator_capacity = int(input())
courses_counter = 0
while number_of_people > 0:
    number_of_people -= elevator_capacity
    courses_counter += 1

    if number_of_people <= 0:
        break

print(courses_counter)
