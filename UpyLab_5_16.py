def my_pow(m,b):

    if not isinstance(m, int) or not isinstance(b, float):
        return None

    return ([b**i for i in range(0, m)])
