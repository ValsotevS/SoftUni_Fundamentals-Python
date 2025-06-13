my_energy = 100
my_coins = 100
bakery_Closed = False
events = input().split("|")

for event in events:
    current_even_list = event.split("-")
    type_of_event = current_even_list[0]
    value_of_event = int(current_even_list[1])

    if type_of_event == "rest":
        energy_gain = value_of_event
        actual_energy_gain = min(energy_gain, 100 - my_energy)
        my_energy += actual_energy_gain
        print(f"You gained {actual_energy_gain} energy.")
        print(f"Current energy: {my_energy}.")

    elif type_of_event == "order":
        if my_energy >= 30:
            my_coins += value_of_event
            my_energy -= 30
            print(f"You earned {value_of_event} coins.")
        else:
            energy_gain = 50
            actual_energy_gain = min(energy_gain, 100 - my_energy)
            my_energy += actual_energy_gain

            print("You had to rest!")

    else:
        if my_coins >= value_of_event:
            my_coins -= value_of_event
            print(f"You bought {type_of_event}.")
        else:
            bakery_Closed = True
            break

if bakery_Closed:
    print(f"Closed! Cannot afford {type_of_event}.")
else:
    print("Day completed!")
    print(f"Coins: {my_coins}")
    print(f"Energy: {my_energy}")
