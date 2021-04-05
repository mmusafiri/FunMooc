def rac_eq_2nd_deg(a, b, c):

    disc = b**2 - 4*a*c

    if disc == 0:
        return (-b/(2*a),)
    if disc > 0:
        rac1 =  (-b - disc ** 0.5) / (2 * a)
        rac2 = (-b + disc ** 0.5) / (2 * a)
        return(min(rac1,rac2), max(rac1,rac2))

    return ()