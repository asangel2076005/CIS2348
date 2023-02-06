lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n\n"))

print(f"Lemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar\n")

desired_servings = float(input("How many servings would you like to make?\n\n"))
servings_divided = servings / desired_servings
lemon_juice = lemon_juice / servings_divided
water = water / servings_divided
agave_nectar = agave_nectar / servings_divided

print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice:.2f} cup(s) lemon juice")
print(f"{water:.2f} cup(s) water")
print(f"{agave_nectar:.2f} cup(s) agave nectar\n")

# 1 gallon = 16 cups
gallon = 16 #cups
print(f"Lemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice / gallon:.2f} gallon(s) lemon juice")
print(f"{water / gallon:.2f} gallon(s) water")
print(f"{agave_nectar / gallon:.2f} gallon(s) agave nectar")


