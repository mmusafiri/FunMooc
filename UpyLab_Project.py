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
    :return: INT pas des zones du chateau
    """
    pas_h = int(abs((ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]) / len(matrix[0])))
    pas_v = int(abs((ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]) / len(matrix)))
    if pas_h <= pas_v:
        return pas_h
    return pas_v


def coordonnees(case, pas):
    """
    :param case: Tuple de la case (X,Y)
    :param pas: pas de la matrice
    :return: Tuple Coordonnées Turtle (X,Y) de la case
    """

    nb_ligne = len(matrice_chateau)

    offset_x = ZONE_PLAN_MINI[0]                        # Récupération offset Turtle en X
    offset_y = ZONE_PLAN_MINI[1]                        # Récuperation offset Turtle en Y

    coord_x = case[1] * pas + offset_x               # Calcul de la Coordonnée abscisse Turtle
    coord_y = (nb_ligne - case[0]) * pas + offset_y    # Calcul de la Coordonnée ordonnée Turtle

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


def tracer_case(case, couleur, pas):
    """
    :param case: Nom de la case à tracer (X,Y)
    :param couleur: Couleur de la case à remplir
    :param pas: pas
    :return:
    """

    turtle.penup()                                      # On leve le stylo
    turtle.goto(coordonnees(case, pas))                 # On se positionne à la coordonnée Turtle de la case
    turtle.color(couleur)                               # On défini la couleur de remplissage
    turtle.begin_fill()                                 # On indique que l'on veut remplir
    tracer_carre(pas-1)                                 # On trace le carré
    turtle.end_fill()                                   # On indique la fin du tracé / remplissage du polygone


def tracer_joueur(case, pas, erase=False):
    turtle.penup()
    centre_joueur = tuple(ti+((pas-1)/2) for ti in coordonnees(case, pas))
    turtle.goto(centre_joueur)
    turtle.pendown()
    if erase:
        coul = COULEUR_VUE
    else:
        coul = COULEUR_PERSONNAGE
    turtle.dot(int(RATIO_PERSONNAGE*(pas-1)), coul)
    turtle.penup()


def affiche_plan(matrix):
    """
    :param matrix: Liste "matricielle" par ligne du Labyrinthe
    :return:
    """

    for Cx, l in enumerate(matrix):                     # Boucle sur les lignes du labyrinthe
        for Cy, c in enumerate(l):                      # Boucle sur les colonnes du labyrinthe
            turtle.speed(0)                             # Initialisation vitesse de traçage
            if int(c) != 0:                             # si la case n'est pas un couloir
                tracer_case((Cx, Cy), COULEURS[int(c)], pas)    # On trace la case
        if Cx == 3:                            # pour debug on affiche pas tout le lab
            break


def deactivate_keyb():
    turtle.onkeypress(None, "Left")  # Désactive la touche Left
    turtle.onkeypress(None, "Right")  # Désactive la touche Left
    turtle.onkeypress(None, "Up")  # Désactive la touche Left
    turtle.onkeypress(None, "Down")  # Désactive la touche Left


def reactivate_keyb():
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


def clean_zone_indice():
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


def indice(pos):

    clean_zone_indice()
    turtle.goto(POINT_AFFICHAGE_ANNONCES)
    turtle.color("black")
    turtle.write("Vous avez trouvé : " + dic_o[pos], font=("Arial", 10, "bold"))


def inventaire(pos):

    global l_inv

    l_inv.append(pos)
    offset = len(l_inv)

    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)
    turtle.color("black")
    turtle.write("Inventaire : ", font=("Arial", 10, "bold"))
    coord = list(POINT_AFFICHAGE_INVENTAIRE)
    coord[1] = coord[1]- offset * 20
    turtle.goto(coord)
    turtle.write("- " + dic_o[pos], font=("Arial", 10, "italic"))
    print()

def check_new_case(pos):
    global matrice_chateau

    if pos in dic_o and matrice_chateau[pos[0]][pos[1]] != 0:
        indice(pos)
        inventaire(pos)
        matrice_chateau[pos[0]][pos[1]] = 0
    if int(matrice_chateau[pos[0]][pos[1]]) == 1:
        return False
    else:
        return True


def next_pos(move):
    new_pos = tuple(el1 + el2 for el1, el2 in zip(position, move))
    if new_pos[0] < 0 or new_pos[0] > len(matrice_chateau) or new_pos[1] < 0 or new_pos[1] > len(matrice_chateau[0]):
        new_pos = position
    return new_pos


def se_deplacer(pos):

    global position

    deactivate_keyb()
    pos_next = next_pos(pos)
    if check_new_case(pos_next):
        tracer_joueur(position, pas, True)
        tracer_joueur(pos_next, pas)
        if position != pos_next:
            tracer_case(position, COULEUR_VUE, pas)
            position = pos_next
    reactivate_keyb()


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
            coord, indice = eval(lig)
            dic_objet.setdefault(coord, indice)
            lig = fl.readline()
    return dic_objet


def main():

    global matrice_chateau, position, dic_o, pas, l_inv

    l_inv = []
    dic_o = creer_dictionnaire_des_objets(fichier_objets)
    position = POSITION_DEPART
    position = (1, 17)
    matrice_chateau = lire_matrice(fichier_plan)
    pas = calcul_pas(matrice_chateau)
    turtle.hideturtle()
    affiche_plan(matrice_chateau)
    tracer_joueur(position, pas)
    attente_deplacement()


if __name__ == "__main__":
    main()
