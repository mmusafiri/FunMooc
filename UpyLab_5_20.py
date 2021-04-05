def verif(mot):
    return ''.join(mot[n] for n in range(len(mot)) if mot[n].isalpha())


def nouveaux_heros(fichier_lecture, fichier_ecriture):

    ANCIEN_HEROS = ("Pierre", "Paul", "Jacqueline")
    NOUVEAU_HEROS = ("Paul", "Tom", "Mathilde")

    with (open(fichier_lecture, encoding="UTF-8")) as fl:
        with (open(fichier_ecriture, 'w', encoding="UTF-8")) as fe:
            ligne = "GO"
            while ligne != "":
                ligne = fl.readline()
                if ligne != "":
                    mot_dans_ligne = []
                    for mot in ligne.split():
                        alpha_mot = verif(mot)
                        if alpha_mot in ANCIEN_HEROS:
                            mot = mot.replace(alpha_mot, NOUVEAU_HEROS[ANCIEN_HEROS.index(alpha_mot)])
                        mot_dans_ligne += [mot]
                    phrase = ' '.join(mot_dans_ligne)+'\n'
                    fe.write(phrase)


nouveaux_heros("histoire_2.txt", "nouvelle_histoire_2.txt")
