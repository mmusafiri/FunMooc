def placer_pion(couleur, colonne, grille):
    for n in range(0,6):
        if grille[n][colonne] == "V":
            grille[n][colonne] = couleur
            return((True, grille))
    return((False, grille))


print(placer_pion('J', 3, [['J', 'J', 'J', 'J', 'J', 'J', 'J'],
                           ['R', 'V', 'R', 'R', 'R', 'V', 'R'],
                           ['R', 'V', 'R', 'J', 'V', 'V', 'V'],
                           ['J', 'V', 'V', 'R', 'V', 'V', 'V'],
                           ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
                           ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))