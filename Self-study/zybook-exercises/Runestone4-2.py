import math
import random

dangle = random.randint(0, 180)
rangle = (dangle * math.pi) / 180
output = math.pow(math.sin(rangle), 2) + math.pow(math.cos(rangle), 2) - 1

print(f"The angle selected at random is {dangle}")
print(f"The value of sin({dangle}) is: {math.sin(rangle)}")
print(f"The value of cos({dangle}) is: {math.cos(rangle)}")
print(f"The value of sin^2({dangle}) + cos^2({dangle}) - 1 is: {math.fabs(output):.1f}")
