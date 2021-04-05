total_age = 0
nb = 0

while 1:
    age_entree = input()
    if age_entree == "-1":
        break
    else:
        total_age = total_age + int(age_entree)
        nb += 1
print(total_age/nb)