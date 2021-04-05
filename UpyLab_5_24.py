def print_mat(matrix):
    aff = ""
    ligne = ""
    for mat in matrix:
        ligne = ""
        for el in mat:
            ligne +=str(el)+" "
        aff += ligne + "\n"
    return(aff)

# ma_matrice = eval(input())
# print(print_mat(ma_matrice))

print(print_mat([['H','E','L','L','O'],['W','O','R','L','D']]))