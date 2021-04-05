def factorielle(n):
    fact = 1
    if n == 0:
        return 1
    for x in range(1,n+1):
        fact *= x
    return fact

def catalan(n):
    return int((factorielle(2*n))/(factorielle(n+1)*factorielle(n)))