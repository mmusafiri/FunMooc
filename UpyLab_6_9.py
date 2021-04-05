def compteur_lettres(texte):
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    dico = dict([(cle, 0) for cle in lettres])

    for l in texte:
        if l.isalpha():
            dico[l.lower()] += 1

    return dico


print(compteur_lettres("Dessine-moi un mouton !"))