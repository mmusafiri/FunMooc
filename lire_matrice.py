def lire_matrice(fichier_encodage):
    with open(fichier_encodage, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier_in]

print(lire_matrice("sudoku1.txt"))