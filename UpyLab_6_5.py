def construction_dict_amis(liste_amis):
    amis = {}
    for prenom1, prenom2 in liste_amis:
        if prenom1 not in amis:
            amis[prenom1] = {prenom2}
        else:
            amis[prenom1].add(prenom2)
        if prenom2 not in amis:
            amis[prenom2] = set()
    return amis

