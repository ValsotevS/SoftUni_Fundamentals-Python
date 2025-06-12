animal_body_list = []

for _ in range(3):
    body_part = input()
    animal_body_list.append(body_part)


animal_body_list[0], animal_body_list[2] = animal_body_list[2], animal_body_list[0]

print(animal_body_list)