def deux_egaux(a, b, c):

    return a == b or b == c or a == c


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    print(deux_egaux(x, y, z))


main()
