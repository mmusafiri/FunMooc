def premier(nb):
    if nb <= 1:
        return False

    for n in range(2, nb):
        if nb % n == 0:
            return False

    return True

def even(num):
    list_even = []
    for n in range(0, num+1):
        if not (n % 2):
            list_even.append(n)
    return (set(list_even))

def prime_numbers(num):
    list_prem = []
    for n in range(2, num+1):
        if premier(n):
            list_prem.append(n)
    return (set(list_prem))

def prime_odd_numbers(numbers):
    liste_premiers = prime_numbers(sorted(numbers)[-1])
    list_even = even(sorted(numbers)[-1])

    nb_premier = set()
    nb_impair = set()
    for num in numbers:
        if num in liste_premiers:
            nb_premier.add(num)
        if num not in list_even:
            nb_impair.add(num)
    return(nb_premier,nb_impair)


# print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
print(prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18]))
print(even(46))