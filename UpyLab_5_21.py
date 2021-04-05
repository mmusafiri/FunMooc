def trim(ligne):
    separators = ("-", "'", "\"", "?", "!", ":", ";", ".", ",", "*", "=", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    for sepa in separators:
        ligne = ligne.replace(sepa, " ")

    return ligne


def liste_des_mots(fichier):
    pass

    with (open(fichier, encoding="UTF-8")) as fl:
        ligne = "GO"
        liste_de_mots = []
        while ligne != "":
            ligne = fl.readline()
            if ligne != "":
                mot_dans_ligne = trim(ligne).split()

                for n in range(len(mot_dans_ligne)):
                    if mot_dans_ligne[n].lower() not in liste_de_mots:
                        liste_de_mots.append(mot_dans_ligne[n].lower())

    return(sorted(liste_de_mots))

liste_des_mots("wc1.txt")