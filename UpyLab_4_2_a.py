def soleil_leve(l, c, a):
    if l == c == 12:
        return False
    if l == c == 0:
        return True
    else:
        if l > c:
            return a >= l or a < c
        return l <= a < c

