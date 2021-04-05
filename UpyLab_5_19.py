def acrostiche(file):

    accro = ""
    with open(file, encoding="UTF-8") as f:
        for line in f:
            accro += (line[0])

    return accro

