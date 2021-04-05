nb = int(input())
nb_char = 1
display = ""
last = 0

for lg in range(nb):

    prespace = " " * (nb-1 - lg)
    number = (1+lg)


    display += str((1+lg) % 10)

    for n in range(1,number):
        display += str((1 + lg + n) % 10)
        last = (1 + lg + n) % 10

    for n in range(1, number):
        display += str((last - n) % 10)

    print(prespace, display, sep="")
    display = ""
