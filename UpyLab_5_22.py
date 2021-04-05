def decompos(ligne):

    for n in range(len(ligne)):
        if not ligne[n].isalnum():
            ligne = ligne.replace(ligne[n], " ")
    return ligne

def wc(fichier):

    with (open(fichier, encoding="UTF-8")) as fl:
        liste_de_mots = []
        nb_lignes = 0
        nb_mots = 0
        nb_caracteres = 0
        ligne = "GO"
        while ligne != "":
            ligne = fl.readline()
            nb_caracteres += len(ligne)
            if ligne != "":
                nb_lignes += 1
                nb_mots += len(decompos(ligne).split())

    return((nb_caracteres, nb_mots, nb_lignes))
