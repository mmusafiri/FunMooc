# importing copy module
import copy


def init_regions(grid):                         # recupere les listes de valeurs de toutes les regions
    dic = {}
    for offsetx in range(0, 3):
        for offsety in range(0, 3):
            lig = []
            for x in range(3):
                for y in range(3):
                    lig.append(grid[x+offsetx*3][y+offsety*3])
            dic[(offsetx,offsety)] = lig
    return dic


def init_row(grid):                             # recupere les listes de valeurs de toutes les lignes
    dic = {}
    n = 0
    for ligne in grid:
        dic[n] = ligne
        n += 1
    return dic


def init_column(grid):                          #recupere les listes de valeurs de toutes les colonnes
    dic = {}
    n = 0
    for col in range(len(grid)):
        colo = []
        for lig in range(len(grid)):
            colo.append(grid[lig][col])
        dic[col] = colo
    return dic


def clear_list(list):                           #enleve les 0 d'une liste et ne garde que les chiffres présents
    to_sendback = []
    for n in range(len(list)):
        if list[n] != 0:
            to_sendback.append(list[n])
    return to_sendback

def offsets(x):                                 # defini les lignes / colonnes complementaires à celle de l'emplacement
    if x % 3 == 0:
        pos_1 = 1
        pos_2 = 2
    elif x % 3 == 1:
        pos_1 = -1
        pos_2 = 1
    elif x % 3 == 2:
        pos_1 = -2
        pos_2 = -1

    return pos_1, pos_2

def re_init(dic_r,dic_c,dic_z,grid):                            # recupere toutes les valeurs de la grilles
    dic_r.clear()                                               # ligne
    dic_r.update(init_row(grid))
    dic_c.clear()                                               # colonne
    dic_c.update(init_column(grid))
    dic_z.clear()                                               # zone
    dic_z.update(init_regions(grid))


def naked_single(grid):

    dic_r = {}
    dic_c = {}
    dic_z = {}
    w_grille = copy.deepcopy(grid)

    re_init(dic_r, dic_c, dic_z, w_grille)                      # On initialise la liste des chiffres de toutes les col/lig/zone de la grille
    loop = 0

    while loop != 81:                                           # Correspond au nombre de boucles max pour tester tous les emplacements
        loop = 0                                                # init a 0
        for x in range(9):                                      # boucle ligne
            for y in range(9):                                  # boucle colonne
                loop += 1
                if w_grille[x][y] == 0:                         # si l'emplacement est vide
                    lst_z = clear_list(dic_z[(x//3, y//3)])     # on recupere l'ensemble des chiffres present de la Zone
                    lst_r = clear_list(dic_r[x])                # on recupere l'ensemble des chiffres present sur la ligne
                    lst_c = clear_list(dic_c[y])                # on recupere l'ensemble des chifffes present sur la colonne

                    p_num = []                                  #init chiffres possibles
                    for n in range(1, 10):                      #on test tous les chiffres de 1 à 9
                        if n not in lst_z and n not in lst_r and n not in lst_c:    # les chiffres possibles non déjà présent
                            p_num.append(n)                                         # dans les 3 listes sont ajoutes

                    if len(p_num) == 1:                         # s'il y a qu'un chiffre possible
                            w_grille[x][y] = p_num[0]           # alors on le rajoute dans la grille
                            re_init(dic_r, dic_c, dic_z, w_grille)  # et on reinit les listes des lignes/colonnes/zones
                            break                               # et on recommence du début

                    elif len(p_num) > 1:                                    # plusieurs chiffres possibles on lance un autre test
                        list_r1_z = clear_list(dic_r[x + offsets(x)[0]])    # on recupere les 2 listes lignes des chiffres dans la zone
                        list_r2_z = clear_list(dic_r[x + offsets(x)[1]])    # ou se situe x,y
                        list_c1_z = clear_list(dic_c[y + offsets(y)[0]])    # idem pour les 2 listes des colonnes
                        list_c2_z = clear_list(dic_c[y + offsets(y)[1]])    # ou se situe x,y

                        p_r_num = []                                        #init de la liste des chiffres possibles côté ligne
                        p_c_num = []                                        #init de la liste des chiffres possibles côté colo
                        for n in p_num:
                            if n in list_r1_z and n in list_r2_z:
                                p_r_num.append(n)                           # si les chiffres possibles sont également dans les 2 lignes
                            if n in list_c1_z and n in list_c2_z:
                                p_c_num.append(n)                           # si les chiffres possibles sont également dans les 2 colonnes
                        if len(p_r_num) == 1:                               # et s'il y en a qu'un côté ligne
                            if w_grille[x][y + offsets(y)[0]] != 0 and w_grille[x][y + offsets(y)[1]] != 0: #on verifie les 2 emplacements adjacent de la ligne sur la zone
                                w_grille[x][y] = p_r_num[0]                 #et s'ils sont pris c'est que c'est le seul emplacement possible
                                re_init(dic_r, dic_c, dic_z, w_grille)      # on reinit les valeurs des lig/col/zone
                                break                                       # et on recommence
                        if len(p_c_num) == 1:                               # idem cote colonnes
                            if w_grille[x + offsets(x)[0]][y] != 0 and w_grille[x + offsets(x)[1]][y] != 0:
                                w_grille[x][y] = p_c_num[0]
                                re_init(dic_r, dic_c, dic_z, w_grille)
                                break

    for n in dic_c:                                                 # on verifie dans toutes les colonnes
        l_c = list(dic_c[n])
        for n in l_c:
            if n == 0:                                              # s'il reste un seul 0
                return (False, None)                                # dans ce cas, pas_chateau de solution
    return(True,w_grille)                                           # sinon on renvoie la solution



#grille = [[0, 0, 6, 0, 4, 0, 1, 0, 0],
#               [0, 5, 0, 0, 9, 0, 0, 6, 0],
#               [8, 0, 0, 0, 0, 0, 0, 0, 5],
#               [0, 0, 0, 3, 0, 4, 0, 0, 0],
#               [3, 1, 0, 0, 0, 0, 0, 4, 8],
#               [0, 0, 0, 8, 0, 7, 0, 0, 0],
#               [6, 0, 0, 0, 0, 0, 0, 0, 9],
#               [0, 2, 0, 0, 3, 0, 0, 5, 0],
#               [0, 0, 1, 0, 5, 0, 7, 0, 0]]


grille =   [[4, 0, 3, 0, 9, 6, 0, 1, 0],
            [0, 0, 2, 8, 0, 1, 0, 0, 3],
            [0, 1, 0, 0, 0, 0, 0, 0, 7],
            [0, 4, 0, 7, 0, 0, 0, 2, 6],
            [5, 0, 7, 0, 1, 0, 4, 0, 9],
            [1, 2, 0, 0, 0, 3, 0, 8, 0],
            [2, 0, 0, 0, 0, 0, 0, 7, 0],
            [7, 0, 0, 2, 0, 9, 8, 0, 0],
            [0, 6, 0, 1, 5, 0, 3, 0, 2]]


print(naked_single(grille))
