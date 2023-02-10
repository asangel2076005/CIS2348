# Angelo Angel (2076005)

import math

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))

wall_area = wall_height * wall_width

print(f"Wall area: {wall_area} square feet")

gallons_of_paint = 350
paint_gallon = wall_area / gallons_of_paint
cans = math.ceil(paint_gallon)

print(f"Paint needed: {paint_gallon:.2f} gallons")
print(f"Cans needed: {cans} can(s)\n")

colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

user_color = input("Choose a color to paint the wall:\n")
print(f"Cost of purchasing {user_color} paint: ${cans * colors[user_color]}")



