import math

centuries = int(input())

years = centuries * 100
days = years * 365.2422
days = math.floor(days)
hours = days * 24
minutes = hours * 60

print(f"{centuries} centuries = {years} years = {math.floor(days)} days = {math.floor(hours)} "
      f"hours = {math.floor(minutes)} minutes")