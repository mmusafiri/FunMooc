import random

def create_map(size, trapsNbr):
    my_map = {}
    if trapsNbr >= size**2:
        return my_map
    TRAP = -1
    MY_PRECIOUS = 1

    n = 1
    while n <= trapsNbr+1:
        if n == trapsNbr+1:
            val = MY_PRECIOUS
        else:
            val = TRAP
        x = random.randint(1, size)
        y = random.randint(1,size)
        if my_map.get((x,y)) != -1:
            my_map[(x,y)] = val
            n +=1
    return my_map

def play_game(map_size, treasure_map):
    """
        reçoit un entier et une carte de taille map_size x map_size, telle que celles obtenues grâce à la fonction create_map, et qui demande à l’utilisateur d’entrer les coordonnées d’une case, jusqu’à tomber sur une case occupée. Si l’utilisateur a trouvé le trésor, la fonction retourne la valeur True, sinon l’utilisateur est tombé sur un piège et la fonction retourne False.
    """
    res = False

    while True:
        coord=input().split()
        x_to_find = int(coord[0])
        y_to_find = int(coord[1])
        if treasure_map.get((x_to_find, y_to_find)) == 1:
            res = True
            break
        elif treasure_map.get((x_to_find, y_to_find)) == -1:
            break

    return res


print(play_game(5, {(3, 4): -1, (4, 1): 1, (2, 3): -1, (1, 5): -1}))