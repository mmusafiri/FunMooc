def trace(M):
    if len(M) == 0:
        return 0

    sum  = 0
    for l,v in enumerate(M):
        sum += v[l]
    return (sum)




t = [[0, 1, 1, 8], [9, 8, 9, 0], [8, 3, 5, 4], [9, 0, 8, 1]]

print(trace(t))