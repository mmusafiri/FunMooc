def symetrie_horizontale(A):

    rep = []
    for l in range(len(A)-1, -1, -1):
        rep = rep + [A[l]]

    return rep


t = [[5, 10, 1], [10, 9, 7], [4, 4, 1]]
print(symetrie_horizontale(t))