a = int(input())
b = int(input())
mise=10
noir = [2, 4, 6, 8, 10, 11]
rouge = [1, 3, 5, 7, 9, 12]


if a <= 12:
    if a == b:
        print(12*mise)
    else:
        print(0)
elif a == 13: #pair
    if not b%2:
        print(2*mise)
    else:
        print(0)
elif a == 14: #impair
    if b%2:
        print(2*mise)
    else:
        print(0)
elif a == 15: #rouge
    if b in rouge:
        print(2*mise)
    else:
        print(0)
elif a == 16: #noir
    if b in noir:
        print(2*mise)
    else:
        print(0)
else:
    pass