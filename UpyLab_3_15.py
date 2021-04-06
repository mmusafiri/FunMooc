nb_barreaux = 100

saut_up = 7
saut_py = 9
saut_lab = 13
position_origine = position_courante = 0


while 1:
    saut = int(input())
    position_cible = int(input())

    if saut < 1 or saut > 99 or position_cible < 1 or position_cible > 99:
        print("pas_chateau dans la plage 1-99")
    else:
        break

while 1:
    position_courante = (position_courante+saut) % nb_barreaux

    if position_courante == position_cible:
        print("Cible atteinte")
        break
    else:
        print(position_courante)

    if position_courante == position_origine:
        print("Pas trouvée")
        break
