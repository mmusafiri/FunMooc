poly = ["T", "C", "O", "D", "I"]
volume = 0
choice = input().upper()
arete = float(input())

if not choice in poly:
    print("Polyèdre non connu")
else:

    if choice == "T":
        volume = 2 ** 0.5 / 12 * arete ** 3
    if choice == "C":
        volume = arete ** 3
    if choice == "O":
        volume = 2 ** 0.5 / 3 * arete ** 3
    if choice == "D":
        volume = (15 + 7 * 5 ** 0.5) / 4 * arete ** 3
    if choice == "I":
        volume = 5 * (3 + 5 ** 0.5) / 12 * arete ** 3
    print(volume)