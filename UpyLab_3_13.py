islist = False
boucle = True
somme = 0
nothingtosum = False

cmd = input()

if cmd == "-1":
    islist = True
else:
    nb_valeur = int(cmd)
    if not nb_valeur:
        nothingtosum = True


if not nothingtosum:

    while boucle:
        valeur_lue = input()

        if str(valeur_lue).upper() == "F" and islist:
            break

        somme += int(valeur_lue)

        if not islist:
            nb_valeur -= 1
            if nb_valeur == 0:
                break

print(somme)
