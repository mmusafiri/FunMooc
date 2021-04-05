import math

point = 0
long = float(input())

while point < 6:
    angle = point * math.pi / 3
    x = long * math.cos(angle)
    y = long * math.sin(angle)
    print(x, y)
    point = point + 1