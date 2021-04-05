def soleil_leve(l, c, a):
    if l == c == 12:
        return False
    if l == c == 0:
        return True
    else:
        if l > c:
            return a >= l or a < c
        return l <= a < c


def main():
    lequinze = int(input())
    cequinze = int(input())
    lesix = int(input())
    cesix = int(input())

    for h in range(24):
        if soleil_leve(lequinze, cequinze, h) or soleil_leve(lesix, cesix, h):
            print(h)
        else:
            print(h, "*")

main()