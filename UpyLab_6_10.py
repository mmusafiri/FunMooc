def valeurs(dico):
    val = []
    for k, v in sorted(dico.items(), key=lambda t: t[0]):
        val.append(v)
    return val

print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))