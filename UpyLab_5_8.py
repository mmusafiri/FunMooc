def isprime(num):
    if num > 2 and num % 2 == 0:
        return False
    for x in range(2, num // 2):
        if num % x == 0:
            return False
    return True


def prime_numbers(nb):
    prem = []

    if not isinstance(nb, int):
        return None

    if nb < 0:
        return None

    if nb >=1:
        num = 2
        while True:
            if isprime(num):
                prem.append(num)
                if len(prem) == nb:
                    break
            num += 1
    return prem
