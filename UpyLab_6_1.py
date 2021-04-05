def inventaire(offres, objets):

    liste_amis = set()

    for obj in objets:
        liste_amis.add(offres[obj])

    return liste_amis
