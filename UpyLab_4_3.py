def premier(nb):
    if nb <= 1:
        return False

    for n in range(2, nb):
        if nb % n == 0:
            return False

    return True


def main():
    x = int(input())

    for n in range(2, x):
        if premier(n):
            print(n)


main()
