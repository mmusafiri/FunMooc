def decompresse(liste_compressee):

    return ([cpl[1] for cpl in liste_compressee for _ in range(cpl[0])])
