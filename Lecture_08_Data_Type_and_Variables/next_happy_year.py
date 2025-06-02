"""You are saying goodbye to your best friend: "See you next happy year".
Happy Year is the year with only distinct digits, for example, 2018.
Write a program that receives an integer number and finds the next happy year."""

year_int = int(input())
next_year = year_int + 1
happy_year_str = ""
is_Happy_Year = False

while not is_Happy_Year:

    year_str = str(next_year)
    for i in year_str:
        num = i
        if num in happy_year_str:
            next_year = int(year_str)
            next_year += 1
            happy_year_str = ""
            break
        else:
            happy_year_str += num
            happy_year_int = int(happy_year_str)
            if happy_year_int == next_year:
                is_Happy_Year = True
                break

print(happy_year_int)
