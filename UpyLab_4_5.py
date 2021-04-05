def rendre_monnaie(prix,vingt,dix,cinq,deux,un):

    somme_versee= 20 * vingt + 10 * dix + 5 * cinq + 2 * deux + un

    if somme_versee < prix:
        return (None, None, None, None, None)

    res20 = divmod(somme_versee - prix, 20)
    res10 = divmod(res20[1], 10)
    res5 = divmod(res10[1], 5)
    res2 = divmod(res5[1], 2)
    res1 = res2[1]

    return(res20[0], res10[0], res5[0], res2[0], res1)