def top_3_candidats(moyennes):

    moyennes_triees = sorted(moyennes.items(), key=lambda moyenne: moyenne[1])
    list=[]

    for n in range(len(moyennes_triees), len(moyennes_triees)-3, -1):
        list.append(moyennes_triees[n-1][0])

    return(tuple(list))

