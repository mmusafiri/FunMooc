from CONFIGS import *
import turtle


def lire_matrice(filename, sep=' '):
    """
    :param filename: nom du fichier
    :param sep: separateur
    :return: list(data_ligne)
    """
    l_plan = []
    with open(filename, 'r', encoding='utf-8') as mon_csvfile:
        for ligne in mon_csvfile:
            l_donnees = ligne.strip().split(sep)
            l_plan.append(l_donnees)
    return l_plan


def calcul_pas(matrix):
    """
    :param matrix: matrice du chateau
    :return: INT pas_chateau des zones du chateau
    """
    pas_h = int(abs((ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]) / len(matrix[0])))
    pas_v = int(abs((ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]) / len(matrix)))
    if pas_h <= pas_v:
        return pas_h
    return pas_v


def coordonnees(case, step):
    """
    :param case: Tuple de la case (X,Y)
    :param step: pas_chateau de la matrice
    :return: Tuple Coordonnées Turtle (X,Y) de la case
    """

    nb_ligne = len(matrice_chateau)

    offset_x = ZONE_PLAN_MINI[0]                        # Récupération offset Turtle en X
    offset_y = ZONE_PLAN_MINI[1]                        # Récuperation offset Turtle en Y

    coord_x = case[1] * step + offset_x               # Calcul de la Coordonnée abscisse Turtle
    coord_y = (nb_ligne - case[0]) * step + offset_y    # Calcul de la Coordonnée ordonnée Turtle

    return coord_x, coord_y


def tracer_carre(dimension):
    """
    :param dimension: la largeur du carré en point pixel Turtle
    :return:
    """
    turtle.pendown()                                    # On pose le stylo
    for _ in range(4):                                  # Boucle de 4 Iterations
        turtle.forward(dimension)                       # On avance de 'dimension'
        turtle.left(90)                                 # On fait 1/4 de tour à droite
    turtle.penup()                                      # On releve le stylo


def tracer_case(case, couleur, step):
    """
    :param case: Nom de la case à tracer (X,Y)
    :param couleur: Couleur de la case à remplir
    :param step: pas_chateau
    :return:
    """

    turtle.penup()                                      # On leve le stylo
    turtle.goto(coordonnees(case, step))                 # On se positionne à la coordonnée Turtle de la case
    turtle.color(couleur)                               # On défini la couleur de remplissage
    turtle.begin_fill()                                 # On indique que l'on veut remplir
    tracer_carre(pas_chateau - 1)                                 # On trace le carré
    turtle.end_fill()                                   # On indique la fin du tracé / remplissage du polygone


def tracer_joueur(case, step, erase=False):
    turtle.penup()
    centre_joueur = tuple(ti + ((pas_chateau - 1) / 2) for ti in coordonnees(case, pas_chateau))
    turtle.goto(centre_joueur)
    turtle.pendown()
    if erase:                                       #TODO : MEM case pour modif couleur erase si deja passé ou non
        coul = COULEUR_CASES
    else:
        coul = COULEUR_PERSONNAGE
    turtle.dot(int(RATIO_PERSONNAGE*(step-1)), coul)
    turtle.penup()


def aff_plan(mat):
    """
    :param mat: Liste "matricielle" par ligne du Labyrinthe
    :return:
    """

    for Cx, l in enumerate(mat):                        # Boucle sur les lignes du labyrinthe
        for Cy, c in enumerate(l):                      # Boucle sur les colonnes du labyrinthe
            turtle.speed(0)                             # Initialisation vitesse de traçage
            if int(c) != 0:                             # si la case n'est pas_chateau un couloir
                tracer_case((Cx, Cy), COULEURS[int(c)], pas_chateau)    # On trace la case
        if Cx == 3:                            # pour debug on affiche pas_chateau tout le lab
            break


def deactiv_keyb():
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    turtle.onkeypress(None, "Right")  # Désactive la touche Left
    turtle.onkeypress(None, "Up")  # Désactive la touche Left
    turtle.onkeypress(None, "Down")  # Désactive la touche Left


def reactiv_keyb():
    turtle.onkeypress(deplacer_gauche, "Left")  # Réassocie la touche Left à la fonction deplacer_gauche
    turtle.onkeypress(deplacer_droite, "Right")  # Réassocie la touche Left à la fonction deplacer_gauche
    turtle.onkeypress(deplacer_haut, "Up")  # Réassocie la touche Left à la fonction deplacer_gauche
    turtle.onkeypress(deplacer_bas, "Down")  # Réassocie la touche Left à la fonction deplacer_gauche


def deplacer_gauche():
    mouvement = (0, -1)
    se_deplacer(mouvement)


def deplacer_droite():
    mouvement = (0, 1)
    se_deplacer(mouvement)


def deplacer_haut():
    mouvement = (-1, 0)
    se_deplacer(mouvement)


def deplacer_bas():
    mouvement = (1, 0)
    se_deplacer(mouvement)


def eff_zone_indice():
    turtle.color(COULEUR_EXTERIEUR)
    turtle.goto(-250, 210)
    turtle.fillcolor(COULEUR_EXTERIEUR)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(2):
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()


def aff_indice(case):

    eff_zone_indice()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.color("black")
    turtle.write("Vous avez trouvé un objet : " + dic_o[case], font=("Arial", 10, "bold"))


def aff_inventaire(case):

    l_inv.append(case)
    offset = len(l_inv)

    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.color("black")
    turtle.write("Inventaire : ", font=("Arial", 10, "bold"))
    coord = list(POINT_AFFICHAGE_INVENTAIRE)
    coord[1] = coord[1] - offset * 20
    turtle.goto(coord)
    turtle.write("N°" + str(offset) + " : " + dic_o[case], font=("Arial", 10, "italic"))
    print()


def verif_nvl_case(case):
    global matrice_chateau

    if case in dic_o and matrice_chateau[case[0]][case[1]] != 5:       # on vérifie si indice et si deja récuperé
        aff_indice(case)
        aff_inventaire(case)
        matrice_chateau[case[0]][case[1]] = 5                         # on definie la nouvelle valeur de la case
    if int(matrice_chateau[case[0]][case[1]]) == 1:                   # si c'est un mur on peut rien faire
        return False
    else:
        return True


def def_nvl_case(mouvement):
    nvl_case = tuple(el1 + el2 for el1, el2 in zip(position, mouvement))
    if nvl_case[0] < 0 or nvl_case[0] > len(matrice_chateau) or nvl_case[1] < 0 or nvl_case[1] > len(matrice_chateau[0]):
        nvl_case = position
    return nvl_case


def se_deplacer(case):

    global position, matrice_chateau

    deactiv_keyb()                                              # on desactive le clavier
    nvl_case = def_nvl_case(case)                               # on calcul la nouvelle case
    if verif_nvl_case(nvl_case):                                # on verifie la nouvelle case
        tracer_joueur(position, pas_chateau, True)              # on efface l'ancienne position joueur
        tracer_joueur(nvl_case, pas_chateau)                    # on affiche sur la nouvelle pos
        if position != nvl_case:                                # si on a changer de case
            tracer_case(position, COULEUR_VUE, pas_chateau)     # on retrace la case precedente
            position = nvl_case                                 # on redefini la position du joueur sur la nouvelle case
    reactiv_keyb()


def attente_deplacement():
    """
    :return:
    """
    turtle.listen()    # Déclenche l’écoute du clavier
    turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left une fonction appelée deplacer_gauche
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")
    turtle.mainloop()    # Place le programme en position d’attente d’une action du joueur


def creer_dictionnaire_des_objets(fichier):
    dic_objet = {}
    with open(fichier, encoding="utf-8") as fl:
        lig = fl.readline()
        while lig != "":
            coord, ind = eval(lig)
            dic_objet.setdefault(coord, ind)
            lig = fl.readline()
    return dic_objet


def main():

    global matrice_chateau, position, dic_o, pas_chateau, l_inv

    l_inv = []
    dic_o = creer_dictionnaire_des_objets(fichier_objets)
    position = POSITION_DEPART
    position = (1, 17)
    matrice_chateau = lire_matrice(fichier_plan)
    pas_chateau = calcul_pas(matrice_chateau)
    turtle.hideturtle()
    aff_plan(matrice_chateau)
    tracer_joueur(position, pas_chateau)
    attente_deplacement()


if __name__ == "__main__":
    main()
