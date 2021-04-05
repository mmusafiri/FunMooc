def calcul_prix(produits, catalogue):

    prix = 0
    for nom_produit in produits:
        if nom_produit in catalogue:
            prix += produits[nom_produit] * catalogue[nom_produit]
    return prix
