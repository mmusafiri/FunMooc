def distance_mots(mot_1,mot_2):
    res = 0
    for n in range (len(mot_1)):
        if mot_1[n] != mot_2[n]:
            res += 1

    return res

def correcteur(mot,listes_mots):

    for m in listes_mots:
        if len(mot) == len(m):
            if distance_mots(mot, m) == 1:
                return m
    return mot

