cards = input().split(" ")
shuffle_count = int(input())

for _ in range(shuffle_count):
    half_deck = len(cards) // 2
    top_half = cards[:half_deck]
    bottom_half = cards[half_deck:]

    shuffled_cards = []

    for i in range(half_deck):
        shuffled_cards.append(top_half[i])
        shuffled_cards.append(bottom_half[i])

    cards = shuffled_cards

print(cards)