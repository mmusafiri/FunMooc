multi=int(input())
res =[]

for ligne in range(1,multi+1):
    for colonne in range(1,multi+1):
        res.append(ligne*colonne)

    for c in range(len(res)):
        print(res[c], sep='\t', end=' ')

    res.clear()
    print()