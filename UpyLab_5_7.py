def plus_grand_bord(w):
    bord = ""
    for n in range(len(w)-1):
        gauche = w[:n+1]
        droite = w[len(w)-1-n:]
        if gauche == droite:
            bord = gauche

    return(bord)
