def verif_good(liste):
    for n in range(1, 10):
        if liste.count(n) != 1:
            return False
    return True


def check_rows(grid):
    for lig in grid:
        if not verif_good(lig):
            return False
    return True


def check_cols(grid):
    for col in range(len(grid)):
        colo = []
        for lig in range(len(grid)):
            colo.append(grid[lig][col])
        if not verif_good(colo):
            return False
    return True


def check_regions(grid):
    for offsetx in range(0, 3):
        for offsety in range(0, 3):
            lig = []
            for x in range(3):
                for y in range(3):
                    lig.append(grid[x+offsetx*3][y+offsety*3])
            if not verif_good(lig):
                return False
    return True


def check_sudoku(grid):
    return check_rows(grid) and check_cols(grid) and check_regions(grid)




grille = [[9, 6, 3, 1, 7, 4, 2, 5, 8],
              [2, 7, 8, 3, 2, 5, 6, 4, 9],
              [1, 5, 4, 6, 8, 9, 7, 3, 1],
              [8, 2, 1, 4, 3, 7, 5, 9, 6],
              [4, 9, 6, 8, 5, 2, 3, 1, 7],
              [7, 3, 5, 9, 6, 1, 8, 2, 4],
              [5, 8, 9, 7, 1, 3, 4, 6, 2],
              [3, 1, 7, 2, 4, 6, 9, 8, 5],
              [6, 4, 2, 5, 9, 8, 1, 7, 3]]
print(check_sudoku(grille))
