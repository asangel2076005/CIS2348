# Angelo Angel 2076005

# Read in first equation, ax + by = c
a = int(input())
b = int(input())
c = int(input())

# Read in second equation, dx + ey = f
d = int(input())
e = int(input())
f = int(input())

check = False

for x in range(-10, 10):
    for y in range(-10, 10):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            check = True
            print(f"{x} {y}")
