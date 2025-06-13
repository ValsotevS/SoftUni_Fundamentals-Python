MAX_ENERGY = 100
ENERGY_COST_PER_ORDER = 30
ENERGY_RECOVERY_WHEN_TIRED = 50

my_energy = 100
my_coins = 100
events = input().split("|")

for event in events:
    current_event_list = event.split("-")
    type_of_event = current_event_list[0]
    value_of_event = int(current_event_list[1])

    if type_of_event == "rest":
        energy_gain = value_of_event
        actual_energy_gain = min(energy_gain, MAX_ENERGY - my_energy)
        my_energy += actual_energy_gain
        print(f"You gained {actual_energy_gain} energy.")
        print(f"Current energy: {my_energy}.")

    elif type_of_event == "order":
        if my_energy >= ENERGY_COST_PER_ORDER:
            my_coins += value_of_event
            my_energy -= ENERGY_COST_PER_ORDER
            print(f"You earned {value_of_event} coins.")
        else:
            energy_gain = ENERGY_RECOVERY_WHEN_TIRED
            actual_energy_gain = min(energy_gain, MAX_ENERGY - my_energy)
            my_energy += actual_energy_gain

            print("You had to rest!")

    else:
        if my_coins < value_of_event:
            print(f"Closed! Cannot afford {type_of_event}.")
            break

        else:
            my_coins -= value_of_event
            print(f"You bought {type_of_event}.")
else:
    print("Day completed!")
    print(f"Coins: {my_coins}")
    print(f"Energy: {my_energy}")