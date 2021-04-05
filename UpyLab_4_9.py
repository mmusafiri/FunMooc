def bat(joueur_1, joueur_2):
    PIERRE = 0
    FEUILLE = 1
    CISEAUX = 2

    if (joueur_1 == PIERRE and joueur_2 == CISEAUX) or (joueur_1 == CISEAUX and joueur_2 == FEUILLE) or (joueur_1 == FEUILLE and joueur_2 == PIERRE):
        return True

    else:
        return False