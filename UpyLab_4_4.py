import random


def alea_dice(s):
    tirage = []
    random.seed(s)
    for _ in range(3):
        tirage.append(random.randint(1, 6))

    if sorted(tirage,reverse=True) == [4, 2, 1]:
        return True
    else:
        return False


