def distance_points(coordonnee_1, coordonnee_2):
    return (((coordonnee_1[0] - coordonnee_2[0]) ** 2 + (coordonnee_1[1] - coordonnee_2[1]) ** 2) ** 0.5)


def longueur(*points):
    nb_points = 1
    lg = 0

    while nb_points < len(points):
        point_origine = points[nb_points - 1]
        point_destination = points[nb_points]
        lg += distance_points(point_origine, point_destination)
        nb_points += 1

    return (lg)


