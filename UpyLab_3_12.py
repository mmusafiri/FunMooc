long=int(input())
nb_blank = 0
for ligne in range(long):
    print(" " * nb_blank + "X"*(long-nb_blank))
    nb_blank += 1