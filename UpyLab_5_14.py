def distance_mots(mot_1,mot_2):
    res = 0
    for n in range (len(mot_1)):
        if mot_1[n] != mot_2[n]:
            res += 1

    return res
