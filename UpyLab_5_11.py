def intersection(v, w):

    mx_chaine=''
    ppc = v
    if len(w) < len(v):
        ppc = w

    for debut in range(len(ppc)):
        for fin in range(debut, len(ppc)):
            sub = v[debut:fin+1]
            if w.find(sub) != -1:
                if len(sub) > len(mx_chaine):
                    mx_chaine = sub

    return mx_chaine
