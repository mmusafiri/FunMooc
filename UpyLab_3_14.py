import random

NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
nb_essai = 1

while 1:
    nb = int(input())

    if nb == secret:
        print("Gagné en {} essai(s) !".format(nb_essai))
        break

    nb_essai += 1

    if nb_essai <= NB_ESSAIS_MAX:
        if nb < secret:
            print("Trop petit")
        elif nb > secret:
            print("Trop grand")
    else:
        print("Perdu ! Le secret était {}".format(secret))
        break
