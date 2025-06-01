your_tasks = str(input())
total_coffee = 0

while your_tasks != "END":

    if your_tasks == "dog" or your_tasks == "cat" or your_tasks == "coding" or your_tasks == "movie":
        total_coffee += 1
    elif your_tasks == "DOG" or your_tasks == "CAT" or your_tasks == "CODING" or your_tasks == "MOVIE":
        total_coffee += 2

    your_tasks = str(input())
if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)