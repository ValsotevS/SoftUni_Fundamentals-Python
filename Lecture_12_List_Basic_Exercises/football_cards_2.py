team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_list = input().split(" ")
game_Terminated = False

for card in cards_list:
    current_card_list = card.split("-")
    if current_card_list[0] == "A":
        if int(current_card_list[1]) in team_A:
            team_A.remove(int(current_card_list[1]))
    elif current_card_list[0] == "B":
        if int(current_card_list[1]) in team_B:
            team_B.remove(int(current_card_list[1]))
    else:
        continue

    if len(team_A) < 7 or len(team_B) < 7:
        game_Terminated = True
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if game_Terminated:
    print("Game was terminated")
