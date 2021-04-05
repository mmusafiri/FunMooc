def gagnant(grille):
    hor = False
    ver = False
    dia = False
    win = ""
    for lin in range (0, 6):
        for col in range(0, 7):
            c = grille[lin][col]
            if c != "V":
                if lin <= 2:
                    count = 1
                    for n in range(1, 4):
                        if grille[lin + n][col] == c:
                            count += 1
                    if count == 4:
                        ver = True
                        win = c
                        break
                #verif vert

                if col <= 3:
                    count = 1
                    for n in range(1, 4):
                        if grille[lin][col+n] == c:
                            count += 1
                    if count == 4:
                        hor = True
                        win = c
                        break

                if col <= 3 and lin <= 2:
                    #verif diagD
                    count = 1
                    for n in range(1, 4):
                        if grille[lin+n][col+n] == c:
                            count += 1
                    if count == 4:
                        dia = True
                        win = c
                        break


                if col >= 3 and lin <=2:
                    #verif diagG
                    count = 1
                    for n in range(1, 4):
                        if grille[lin + n][col - n] == c:
                            count += 1
                    if count == 4:
                        dia = True
                        win = c
                        break

    print(hor,ver,dia)
    if hor or ver or dia:
        return win
    else:
        return None


print(gagnant([['V', 'V', 'R', 'J', 'V', 'R', 'J'],
         ['V', 'V', 'V', 'R', 'V', 'R', 'R'],
         ['V', 'V', 'R', 'V', 'R', 'J', 'J'],
         ['V', 'V', 'R', 'V', 'V', 'J', 'J'],
         ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
         ['V', 'V', 'V', 'J', 'V', 'V', 'V']]))