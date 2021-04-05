def symetrise_amis(dic, englobe):

    global d

    for personne, amis in dic.items():
        disc = set()
        for ami in amis:
            if englobe:
                if ami not in dic:
                    dic.update(ami, personne)
                else:
                    if not personne in dic[ami]:
                        dic[ami].add(personne)
            else:
                if ami in dic and ami != personne:
                    disc.add(ami)
        if not englobe:
            for name_disc in disc:
                dic[personne].discard(name_disc)
    d = dic
    return None


# d = {'Thierry': {'Michelle', 'Bernadette'}, 'Michelle': {'Thierry'}, 'Bernadette': set()}
# #d = {'Thierry': {'Thierry'}, 'Quidam': {'Ariane'}, 'Ariane': {'Thierry'}}
#d = {'Michelle': {'Ariane'}, 'Pierre': {'Ariane'}, 'Bernadette': {'Bernadette'}, 'Ariane': {'Bernadette'}}

#d = {'Thierry': {'Quidam', 'Michelle'}, 'Quidam': set(), 'Michelle': set(), 'Bernadette': {'Michelle', 'Bernadette'}}
# {'Thierry': set(), 'Quidam': set(), 'Michelle': set(), 'Bernadette': {'Bernadette'}}

d = {'Pierre': {'Michelle'}, 'Ariane': {'Ariane', 'Michelle'}, 'Michelle': set(), 'Bernadette': {'Ariane'}}
#{'Pierre': {'Michelle'}, 'Ariane': {'Ariane', 'Michelle', 'Bernadette'}, 'Michelle': {'Pierre', 'Ariane'}, 'Bernadette': {'Ariane'}}

#d = {'Thierry': {'Ariane'}, 'Bernadette': set(), 'Michelle': {'Bernadette'}, 'Ariane': set(), 'Pierre': {'Ariane', 'Bernadette'}}
#{'Thierry': set(), 'Ariane': set(), 'Pierre': set(), 'Michelle': set(), 'Bernadette': set()

#d = {'Thierry': {'Quidam'}, 'Quidam': {'Pierre'}, 'Michelle': {'Pierre'}, 'Pierre': {'Thierry'}}
#{'Thierry': {'Quidam', 'Pierre'}, 'Quidam': {'Thierry', 'Pierre'}, 'Michelle': {'Pierre'}, 'Pierre': {'Thierry', 'Quidam', 'Michelle'}}
symetrise_amis(d, True)

print(d)
