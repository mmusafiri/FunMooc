#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MOOC PROJECT - CHATEAU DU PYTHON DES NEIGES

Parcours du labyrinthe à la recherche d'indice.
Répondre aux questions pour traverser les portes.
Cliquer sur l'écran  en fin pour sortir

Chaque Fonction est documentée
"""

__author__ = "Nicolas RISSOAN"
__copyright__ = "© 2021/04"
__credits__ = ["FUN MOOC TEAM"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Ashofphoenix"
__email__ = "ashofphoenix@sunnox.fr"
__status__ = "Prototype"


# DECLARATION IMPORTS

from CONFIGS import *
import turtle

# DECLARATION VARIABLES GLOBALES

l_inv = []                                              # Liste d'objets trouvés
dic_o = {}                                              # Dict objet du chateau
dic_q = {}                                              # Dict question du chateau
mat_chateau = []                                        # List matrice du chateau
pos_joueur = ()                                         # position joueur
pas_chateau = 0                                         # pas pour déplacement
triche = False                                          # Indication de Triche
triche_index = 0                                        # Index de Triche
triche_pos = ()                                         # Position de Triche


# FONCTIONS


def lire_matrice(filename, sep=' '):
    """
    lit le fichier du labyrinthe et crée une liste "matrice"
    :param filename: nom du fichier
    :param sep: separateur
    :return: list(data_ligne)
    """
    l_plan = []                                         # Initialisation liste vide
    with open(filename, 'r', encoding='utf-8') as fm:   # Ouverture du fichier plan
        for ligne in fm:                                # lecture par ligne
            l_donnees = ligne.strip().split(sep)        # Séparation des données en liste
            l_plan.append([int(x) for x in l_donnees])  # Ajout dans la liste en format INT
    return l_plan                                       # Renvoi de la liste


def calcul_pas(matrix):
    """
    Calcul du pas de la matrice. Ce pas ne varie plus et est passé en variable globale pour certains cas
    :param : matrice du chateau
    :return: INT pas_chateau des zones du chateau
    """
    pas_h = abs((ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0]) / len(matrix[0]))  # Calcul du pas en X
    pas_v = abs((ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1]) / len(matrix))     # Calcul du pas en Y
    return int(min(pas_h, pas_v))                                          # Renvoi du pas le plus petit


def coordonnees(case, step):
    """
    Calcul des coordonnées Turtle d'une case
    :param case: Tuple de la case (X,Y)
    :param step: pas_chateau de la matrice
    :return: Tuple Coordonnées Turtle (X,Y) de la case
    """

    nb_ligne = len(mat_chateau)                         # Récuperation Nb de lignes matrice pour calcul offset ordonnées

    offset_x = ZONE_PLAN_MINI[0]                        # Récupération offset Turtle en X
    offset_y = ZONE_PLAN_MINI[1]                        # Récuperation offset Turtle en Y

    coord_x = case[1] * step + offset_x                 # Calcul de la Coordonnée abscisse Turtle
    coord_y = (nb_ligne - case[0]) * step + offset_y    # Calcul de la Coordonnée ordonnée Turtle

    return coord_x, coord_y


def tracer_carre(dimension):
    """
    :param dimension: la largeur du carré en point pixel Turtle
    :return:
    """
    turtle.pendown()                                    # Descente du stylo
    for _ in range(4):                                  # Boucle de 4 Iterations
        turtle.forward(dimension)                       # Avancer
        turtle.left(90)                                 # Rotation 90°
    turtle.penup()                                      # Montée du stylo


def tracer_case(case, couleur, step):
    """
    Trace la case que l'on veut de la couleur que l'on veut
    :param case: Nom de la case à tracer (X,Y)
    :param couleur: Couleur de la case à remplir
    :param step: pas_chateau (Sachant que pas_chateau est en global, on pourrait réécrire la fonction sans ce paramètre
    :return:
    """
    turtle.penup()                                      # Montée de stylo
    turtle.goto(coordonnees(case, step))                # Positionnement aux coordonnées Turtle de la case
    turtle.pendown()                                    # Descente du stylo
    turtle.color(COULEUR_EXTERIEUR, couleur)            # Définition de la couleur de contour et de remplissage
    turtle.begin_fill()                                 # Début remplissage
    tracer_carre(pas_chateau)                           # Tracage du carré
    turtle.end_fill()                                   # Fin du remplissage
    turtle.penup()                                      # Montée du stylo


def aff_joueur(case, efface=False):
    """
    Affiche le rond du joueur
    :param case: Tuple Case sur laquelle le joueur doit être affiché
    :param efface: Boolean True = On 'efface' en redessinant le joueur avec la couleur de fond de la case
    :return:
    """
    turtle.penup()                                      # Montée du stylo
    centre_joueur = tuple(ti + (pas_chateau / 2) for ti in coordonnees(case, pas_chateau))  # Calcul coord
    turtle.goto(centre_joueur)                          # Positionnement aux coordonnées
    turtle.pendown()                                    # Descente du stylo
    if efface:                                          # Vérification si effacement
        coul = COULEURS[mat_chateau[case[0]][case[1]]]  # Récupération de la couleur de la case
    else:                                               # Sinon
        coul = COULEUR_PERSONNAGE                       # Initialisation couleur personnage
    turtle.dot(int(RATIO_PERSONNAGE * pas_chateau), coul)  # On fait le rond du personnage avec le ratio
    turtle.penup()                                      # Montée du Stylo


def aff_plan(mat):
    """
    Affichage du plan du labyrinthe

    :param mat: Liste "matricielle" par ligne du Labyrinthe
    :return:
    """

    for Cx, l in enumerate(mat):                        # Boucle sur les lignes du labyrinthe
        for Cy, c in enumerate(l):                      # Boucle sur les colonnes du labyrinthe
            tracer_case((Cx, Cy), COULEURS[c], pas_chateau)  # On trace la case



def eff_zone_indice():
    """
    Efface la zone d'indice : en fait, dessine un rectangle par dessus de la même couleur que le fond
    :return:
    """
    turtle.penup()                                      # Montée du stylo
    turtle.color(COULEUR_EXTERIEUR)                     # Définition de la couleur du stylo
    turtle.goto(-250, 230)                              # Positionnement pour début tracage
    turtle.fillcolor(COULEUR_EXTERIEUR)                 # Définition de la couleur de remplissage
    turtle.begin_fill()                                 # Début remplissage
    turtle.pendown()                                    # Descente du stylo
    for _ in range(2):                                  # Dessin d'un rectangle
        turtle.forward(600)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()                                   # Fin Remplissage
    turtle.penup()                                      # Montée du stylo


def aff_indice(case, typemes=0):
    """
    Permet l'affichage de l'indice ou d'autres messages
    :param case: case pour recuperer l'objet. Si case = (-1,-1) alors typemes sera utilisé pour d'autres messages
    :param typemes: INT suivant le type de message à afficher
    :return:
    """
    eff_zone_indice()                                   # Effacement de la zone d'indice
    turtle.penup()                                      # Montée du stylo
    turtle.goto(POINT_AFFICHAGE_ANNONCES)               # Positionnement au point d'affichage de l'annonce
    turtle.color("black")                               # Définition de la couleur
    message = ""                                        # Initialisation message vide
    ft = ("Arial", 10, "bold")                          # Initialisation Police de caractères par défaut
    if case != (-1, -1):                                # Vérification 'vraie' case
        message = "Vous avez trouvé un objet : " + dic_o[case]  # Message Objet trouvé
    else:                                               # Sinon case = (-1,-1) > autre message
        if typemes == 0:                                # Type 0
            message = "Cette porte est fermée."         # Message porte fermée
        elif typemes == 1:                              # Type 1
            message = "La porte s'ouvre !"              # Message porte ouverte
        elif typemes == 2:                              # Type 2
            message = "Mauvaise réponse !"              # Message mauvaise réponse
        elif typemes == 3:                              # Type 3
            message = "Vous n'avez pas tous les indices ! Ils vous les faut tous !"  # Pas assez d'indices
        elif typemes == 4:                              # Type 4
            message = "FELICITATIONS ! - Cliquez pour quitter" # Félicitations
            ft = ("Arial", 15, "bold")                  # Police plus grosse

    turtle.write(message, font=ft)                      # Ecriture du message


def aff_inventaire(case):
    """
    Affichage de l'inventaire de la case
    :param case: tuple de la case
    :return:
    """
    l_inv.append(case)                                  # Ajout case a list inventaire trouvé
    offset = len(l_inv)                                 # Nombre d'objet trouvé

    turtle.penup()                                      # Montée du stylo
    turtle.goto(POINT_AFFICHAGE_INVENTAIRE)             # Positionnement au point d'affichage
    turtle.color("black")                               # Définition couleur d'affichage

    if offset <= 1:                                     # Si premier objet trouvé
        turtle.write("Inventaire : ", font=("Arial", 10, "bold"))   # Ecriture 'Inventaire' en titre
    coord = list(POINT_AFFICHAGE_INVENTAIRE)            # Initialisation coordonnée point affichage en list
    coord[1] = coord[1] - offset * 20                   # Application de l'offset d'affichage en Y pour liste objet
    turtle.goto(coord)                                  # Positionnement au point d'affichage inventaire
    turtle.write("N°" + str(offset) + " : " + dic_o[case], font=("Arial", 10, "italic"))  # Affichage dernier objet


def aff_question(case):
    """
    Affiche la question de la case
    :param case: tuple position case
    :return: Boolean True = bonne réponse / False = mauvaise réponse
    """
    aff_indice((-1, -1), 0)                             # Affichage Indice porte fermée
    reponse = turtle.textinput("Question", dic_q[case][0]) == dic_q[case][1]    # Boolean Rep correct à Quest. case

    if reponse or triche:                               # Bonne réponse (OU TRICHE !!)
        aff_indice((-1, -1), 1)                         # Affichage Indice porte ouverte
        return True                                     # Renvoi Boolean Bonne réponse
    else:                                               # Mauvaise réponse
        aff_indice((-1, -1), 2)                         # Affichage Indice mauvaise réponse
    return False                                        # Renvoi Boolean mauvaise réponse


def verif_nvl_case(case):
    """
    verification de la nouvelle case et des différentes possibilités
    :param case: case à vérifier
    :return: Boolean : True = case accessible, False = case inaccessible
    """
    if mat_chateau[case[0]][case[1]] == 1:              # Vérification mur
        return False                                    # Case inaccessible
    else:
        if mat_chateau[case[0]][case[1]] != 5:          # Case non déjà explorée

            if case in dic_o:                           # Case avec indice
                aff_indice(case)                        # Affichage indice
                if len(l_inv) <= len(dic_o):            # Verification avant affichage inventaire (pour mode triche)
                    aff_inventaire(case)                # Affichage dans l'inventaire

            if case in dic_q:                           # Case avec Question / Porte
                if not aff_question(case):              # Mauvaise réponse
                    return False                        # case inaccessible

            if mat_chateau[case[0]][case[1]] == 2:      # Cas spécifique : Si la case est la sortie
                if len(l_inv) < len(dic_o):             # Manque d'indice
                    aff_indice((-1, -1), 3)             # Affichage Sortie Impossible
                    return False                        # Case inaccessible
                aff_indice((-1, -1), 4)                 # Affichage Final félicitations
        return True                                     # Case accessible


def def_nvl_case(mouvement):
    """
    Renvoi la valeur de la case à atteindre par le joueur apres le mouvement
    :param mouvement: Offset en abscisse et ordonnee par rapport à la position actuelle
    :return: Tupe nouvelle case
    """
    nvl_case = tuple(el1 + el2 for el1, el2 in zip(pos_joueur, mouvement))  # Calcul de la nouvelle case
    if nvl_case[0] < 0 or nvl_case[0] > len(mat_chateau) or nvl_case[1] < 0 or nvl_case[1] > len(
            mat_chateau[0]):                            # Si la nouvelle case est HORS limite
        nvl_case = pos_joueur                           # du chateau alors on ne change pas de case
    return nvl_case                                     # renvoie de la nouvelle case


def se_deplacer(mouvement):
    """
    Mise a jour de la position du joueur sur la carte et Mise à jour de la carte
    Des vérifications seront effectuées avant
    :param mouvement: offset de case envisagé pour le déplacement
    :return:
    """
    global pos_joueur, mat_chateau, triche

    deactiv_keyb_fleches()                              # Désactivation du clavier

    if triche:                                          # Si triche
        nvl_case = triche_pos                           # La nouvelle position sera celle de triche
    else:
        nvl_case = def_nvl_case(mouvement)              # Sinon on calcul la nouvelle case avec l'offset de mouvement

    if verif_nvl_case(nvl_case):                        # Si déplacement possible sur nouvelle case
        if pos_joueur != nvl_case:                      # si la position du joueur et différente de la case où on va
            aff_joueur(pos_joueur, True)                # Effacement de l'ancienne position joueur
            aff_joueur(nvl_case)                        # Positionnement du joueur sur la nouvelle case
            mat_chateau[pos_joueur[0]][pos_joueur[1]] = 5  # on défini l'ancienne case comme "visitée" dans la matrice
            tracer_case(pos_joueur, COULEUR_VUE, pas_chateau)  # on retrace la case precédente la couleur "VUE"
            pos_joueur = nvl_case                       # On redéfini la position joueur comme etant cette nouvelle case
            triche = False                              # Triche désactivée

    if mat_chateau[pos_joueur[0]][pos_joueur[1]] == 2:  # Si la nouvelle  position est la sortie
        # turtle.done()                                 # C'est la fin !
        turtle.exitonclick()                            # attente un click de souris

    reactiv_keyb_fleches()                              # Reactivation du clavier

def deplacer_triche(dico):
    """
    Permet de tricher sur les déplacements en passant d'un emplacement à un autre sans parcours
    :return:
    """
    global triche_index, pos_joueur, triche, triche_pos

    triche = True                                       # On triche !!!
    mouvement = (0, 0)                                  # Pas de mouvement envisagé

    if triche_index >= len(dico):                       # Si l'index de triche dépasse le nb d'objets
        triche_index = 0                                # On réinitialise l'index de triche par rapport au dictionnaire
    for count, valeurs in enumerate(dico.items()):      # On parcourt le dictionnaire
        if triche_index == count:                       # Lorsqu'on trouve l'index
            triche_pos = valeurs[0]                     # On sauvegarde la position de triche
            triche_index += 1                           # On augmente l'index pour le prochain appui
            break                                       # On sort de la boucle
    se_deplacer(mouvement)                              # On lance la fonction de deplacement


def deplacer_gauche():
    """
    Défini le mouvement de case à envisager par rapport à la case actuelle et la numérotation des cases
    :return
    """
    mouvement = (0, -1)                                 # -1 en abscisse
    se_deplacer(mouvement)                              # Lance la fonction de déplacement


def deplacer_droite():
    """
    Défini le mouvement de case à envisager par rapport à la case actuelle
    :return
    """
    mouvement = (0, 1)                                  # +1 en abscisse
    se_deplacer(mouvement)                              # Lance la fonction de déplacement


def deplacer_haut():
    """
    Défini le mouvement de case à envisager par rapport à la case actuelle
    :return
    """
    mouvement = (-1, 0)                                 # -1 en ordonnée
    se_deplacer(mouvement)                              # Lance la fonction de déplacement


def deplacer_bas():
    """
    Défini le mouvement de case à envisager par rapport à la case actuelle
    :return
    """
    mouvement = (1, 0)                                  # +1 en ordonnée
    se_deplacer(mouvement)                              # Lance la fonction de déplacement


def deplacer_triche_questions():
    """
    Lance la fonction de triche de déplacement sur chaque question (dictionnaire d'objets)
    :return:
    """
    deplacer_triche(dic_q)


def deplacer_triche_objets():
    """
    Lance la fonction de triche de déplacement sur chaque objets (dictionnaire d'objets)
    :return:
    """
    deplacer_triche(dic_o)


def deactiv_keyb_fleches():
    """
    Désactivation des actions possibles lors d'appuis touche sur les touches de déplacement (flèches)
    :return:
    """
    turtle.onkeypress(None, "Left")                     # Désactive la touche Left
    turtle.onkeypress(None, "Right")                    # Désactive la touche Right
    turtle.onkeypress(None, "Up")                       # Désactive la touche Up
    turtle.onkeypress(None, "Down")                     # Désactive la touche Down
    turtle.onkeypress(None, "o")                        # Désactive la touche o TRICHE objets
    turtle.onkeypress(None, "q")                        # Désactive la touche q TRICHE question


def reactiv_keyb_fleches():
    """
    Réactivation des actions possibles  lors d'appuis touche sur les touches de déplacement (flèches)
    :return:
    """
    turtle.listen()
    turtle.onkeypress(deplacer_gauche, "Left")          # Réassocie la touche Left à la fonction deplacer_gauche
    turtle.onkeypress(deplacer_droite, "Right")         # Réassocie la touche Right à la fonction deplacer_droite
    turtle.onkeypress(deplacer_haut, "Up")              # Réassocie la touche Up à la fonction deplacer_haut
    turtle.onkeypress(deplacer_bas, "Down")             # Réassocie la touche Down à la fonction deplacer_bas
    turtle.onkeypress(deplacer_triche_objets, "o")      # Réassocie la touche o à la fonction deplacer_triche_objets
    turtle.onkeypress(deplacer_triche_questions, "q")   # Réassocie la touche q à la deplacer_triche_questions


def attente_deplacement():
    """
    Boucle d'attente de déplacement
    :return:
    """

    turtle.listen()                                     # Déclenche l’écoute du clavier
    turtle.onkeypress(deplacer_gauche, "Left")          # Associe à la touche Left une fonction appelée deplacer_gauche
    turtle.onkeypress(deplacer_droite, "Right")         # Associe à la touche Right une fonction appelée deplacer_droite
    turtle.onkeypress(deplacer_haut, "Up")              # Associe à la touche Up une fonction appelée deplacer_haut
    turtle.onkeypress(deplacer_bas, "Down")             # Associe à la touche Down une fonction appelée deplacer_bas
    turtle.onkeypress(deplacer_triche_objets, "o")      # Associe une touche pour tricher pour les objets
    turtle.onkeypress(deplacer_triche_questions, "q")   # Associe une touche pour tricher pour les questions
    turtle.mainloop()                                   # Place le programme en attente d’une action sur les touches


def creer_dict(fichier):
    """
    Création des dictionnaires à partir des fichiers
    :param fichier: nom du fichier contenant les paramètres à lire
    :return: dict ((coord), "valeur")
    """
    dico = {}                                           # Init d'un dico vide
    with open(fichier, 'r', encoding="utf-8") as fl:    # Ouverture du fichier
        for ligne in fl:                                # boucle sur chaque ligne
            cle, valeur = eval(ligne)                   # On récupère les données dans deux variables
            dico.setdefault(cle, valeur)                # On les rajoute au dictionnaire
    return dico                                         # Renvoi dictionnaire crée


def init():
    """
    INITIALISATION init des différentes variables globales et lancement de la boucle Turtle d'attente clavier
    :return:
    """
    global mat_chateau, pos_joueur, dic_o, pas_chateau, dic_q

    dic_o = creer_dict(fichier_objets)                  # Dictionnaire des objets
    dic_q = creer_dict(fichier_questions)               # Dictionnaire des questions
    pos_joueur = POSITION_DEPART                        # Position de départ du joueur
    mat_chateau = lire_matrice(fichier_plan)            # Création de la matrice du plan du chateau
    pas_chateau = calcul_pas(mat_chateau)               # Pas des positions du chateau

    turtle.title("Chateau du Python des Neiges - © AshOfPhoenix")  # Change le titre
    turtle.tracer(0, 0)                                 # désactive les delais d'affichage et animation
    turtle.bgcolor(COULEUR_EXTERIEUR)                   # Initialisation couleur de fond Turtle
    aff_plan(mat_chateau)                               # Affichage du plan
    aff_joueur(pos_joueur)                              # Affichage du joueur
    attente_deplacement()                               # Lancement de la boucle d'attente de déplacement 'Turtle'


if __name__ == "__main__":
    init()
