import math
def bonne_planete(diametre):
    if math.pi * diametre**2 >= NB_GRAINE * AIRE_MINI:
        return True
    else:
        return False

NB_GRAINE = 1000
AIRE_MINI = 50

def main():

    dia = int(input())
    if bonne_planete(dia):
        print("Bonne planète")
    else:
        print("Trop petite")

if __name__ == "__main__":
    main()
