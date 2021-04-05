def anagrammes(v, w):

    if len(v) != len(w):
        return False

    if sorted(list(v)) == sorted(list(w)):
        return True
    else:
        return False

