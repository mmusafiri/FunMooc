def file_histogram(filename):
    dic = {}
    with open(filename, encoding="utf-8") as f:
        ligne = f.readline()
        while ligne != "":
            for l in ligne:
                if l not in dic:
                    dic[l] = 1
                else:
                    dic[l] += 1
            ligne = f.readline()
        return dic


def trim(element):
    separators = ("-", "'", "\"", "?", "!", ":", ";", ".", ",", "*", "=", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    for sepa in separators:
        element = element.replace(sepa, " ")
    return element.strip().split()


def words_by_length(filename):
    dic = {}
    with open(filename, encoding="utf-8") as f:
        ligne = f.readline()
        while ligne != "":
            mots = ligne.split()
            for mot in mots:
                lmot = trim(mot)
                for m in lmot:
                    if len(m) not in dic:
                        dic[len(m)] = [m.lower()]
                    else:
                        if m.lower() not in dic[len(m)]:
                            dic[len(m)].append(m.lower())


            ligne = f.readline()
        for m in dic:
            dic[m] = sorted(dic[m])
        return dict(sorted(dic.items(), key=lambda t: t[0]))


ret = words_by_length("Zola.txt")
ret_v = {1: ['a', 'c', 'd', 'l', 'n', 's', 'à'], 2: ['ce', 'de', 'du', 'en', 'et', 'il',
     'la', 'le', 'là', 'sa', 'se', 'si', 'un'],
 3: ['aux', 'des', 'ils', 'les', 'par', 'pas_chateau',
     'que', 'qui', 'ses', 'sol', 'une', 'vie'],
 4: ['avec', 'blés', 'ciel', 'dans', 'dont',
     'loin', 'plus', 'pour', 'sous', 'sève',
     'tous', 'voix'],
 5: ['armée', 'astre', 'avril', 'bruit', 'cette',
     'comme', 'coups', 'faire', 'flanc', 'futur',
     'grand', 'haies', 'noire', 'parts', 'pieds',
     'pièce', 'plein', 'terre', 'vives', 'était'],
 6: ['allait', 'arbres', 'autres', 'baiser', 'besoin',
     'cassée', 'champs', 'chaque', 'droite', 'encore',
     'gauche', 'germes', 'gloire', 'grosse', 'herbes',
     'hommes', 'jeunes', 'plaine', 'rauque', 'rayons',
     'rumeur', 'siècle', 'soleil', 'suivre', 'toutes',
     'vertes', 'échine'],
 7: ['bientôt', 'chaleur', 'coulait', 'croyait',
     'fussent', 'germait', 'graines', 'lumière',
     'maheude', 'matinée', 'montait', 'poussée',
     'sillons', 'souffle', 'éclater', 'étaient'],
 8: ['campagne', 'enjambée', 'feuilles', 'jeunesse',
     'obstinés', 'profonds', 'récoltes', 'tapaient', 'épandait'],
 9: ['bourgeons', 'camarades', 'crevaient', 'enfantait', 'enflammés',
     'entendait', 'gerçaient', 'lentement', 'rayonnait'],
 10: ['accompagné', 'betteraves', 'gonflaient', 'maintenant',
      'nourricier', 'poussaient', 'rapprochés', 'rivelaines',
      'ronflement', 'vengeresse', 'échauffant'],
 11: ['débordement', 'germination', 'grandissant', 'jaillissait',
      'reconnaître', 'travaillées', 'ventilateur'],
 12: ['allongeaient', 'chuchotantes', 'continuaient'],
 13: ['distinctement'], 14: ['tressaillaient']}
print(ret==ret_v)
print(ret_v)
print(ret)


