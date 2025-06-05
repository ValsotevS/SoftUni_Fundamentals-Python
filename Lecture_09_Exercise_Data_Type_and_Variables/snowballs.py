number_of_snowballs = int(input())

highest_ball_rating = 0

weight_of_highest_rated = 0
time_of_highest_rated = 0
quality_of_highest_rate = 0

for ball in range(number_of_snowballs):
    weight_of_ball = int(input())
    time_to_target = int(input())
    quality_of_ball = int(input())

    ball_rating = (weight_of_ball / time_to_target) ** quality_of_ball

    if ball_rating > highest_ball_rating:
        highest_ball_rating = ball_rating
        weight_of_highest_rated = weight_of_ball
        time_of_highest_rated = time_to_target
        quality_of_highest_rate = quality_of_ball

print(f"{weight_of_highest_rated} : {time_of_highest_rated} = {int(highest_ball_rating)} ({quality_of_highest_rate})")
