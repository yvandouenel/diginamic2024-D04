from math import sqrt

# Créer une fonction square_root prenant un nombre en paramètre, et retournant la racine carrée de ce nombre (vous pouvez utiliser le module math)
# Printer l'appel de la fonction avec un nombre donné


def square_root(nb):
    return sqrt(nb)


print(square_root(9))

# Créer une fonction extendator ne prenant aucun paramètre, et qui ne retourne rien.
# Faire en sorte qu'elle modifie la liste suivante définie dans l'espace global en l'étendant de la liste suivante [4, 5, 6]
liste_depart = [1, 2, 3]


# fonction impure car elle modifie une liste déjà existante
def extendator():
    liste_depart.extend([4, 5, 6])


extendator()
print(liste_depart)

# Créer une fonction add prenant en paramètres deux nombres et qui retourne l'addition de ses deux nombres
# Créer une fonction carre qui prend un nombre en paramètre et retourne ce dernier élevé au carré
# A l'aide de ses deux fonction, retourner la somme des carrés de 2 et 3 (2² + 3²)
# Printer le résultat


# Pas de collision de nom de variable car a et b ne sont définis que dans la fonction add
def add(a, b):
    return a + b


# Pas de collision de nom de variable car a n'est défini que dans la fonction carre
def carre(a):
    return a * a


result = add(carre(2), carre(3))
print(result)
