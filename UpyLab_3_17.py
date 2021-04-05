addition = True
epsi = 10 ** -6
puissance = 1
sinus = 0

def factorielle(n):
    if n == 0:
        return 1
    else:
        F = 1
        for k in range(2,n+1):
            F = F * k
        return F

valeur = float(input())


while 1:
    terme = (valeur**puissance)/factorielle(puissance)

    if abs(terme) < epsi:
        break

    if not addition:
        sinus -= terme
    else:
        sinus += terme

    addition = not addition
    puissance += 2

print(sinus)
