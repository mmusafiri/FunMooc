def est_adn(chaine):

    brin = ("A", "C", "G", "T")

    for c in chaine:
        if c not in brin:
            return False
    if len(chaine) == 0:
        return False
    else:
        return True

