import random


def bat(joueur_1, joueur_2):
    PIERRE = 0
    FEUILLE = 1
    CISEAUX = 2

    if (joueur_1 == PIERRE and joueur_2 == CISEAUX) or (joueur_1 == CISEAUX and joueur_2 == FEUILLE) or (
            joueur_1 == FEUILLE and joueur_2 == PIERRE):
        return True

    else:
        return False


def main():
    nom_coup = ("Pierre", "Feuille", "Ciseaux")
    points = 0
    coup_j = []

    s = int(input())
    for _ in range(5):
        coup_j.append(int(input()))

    random.seed(s)
    for x in range(5):
        coup_o = int(random.randint(0, 2))

        if bat(coup_o, coup_j[x]):
            verbe = "bat"
            points -= 1
        elif coup_o != coup_j[x]:
            verbe = "est battu par"
            points += 1
        else:
            verbe = "annule"

        print(nom_coup[coup_o], verbe, nom_coup[coup_j[x]], ":", points)

    if points < 0:
        print("Perdu")
    elif points == 0:
        print("Nul")
    elif points > 0:
        print("Gagné")


main()
