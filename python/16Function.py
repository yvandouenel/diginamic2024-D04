from pprint import pprint
from math import sqrt


""" def faire_un_truc():
    # la portée ou le scope de la variable variable_locale est la fonction faire_un_truc
    variable_locale = 12
    print("Espace local de l'intérieur de la fonction faire_un_truc: ")
    # pprint(locals())

    print("Espace global vu depuis la fonction faire_un_truc: ")
    # pprint(globals())

    return f"Je fais un truc avec {variable_locale}."


pi = 3.14

print(faire_un_truc())

# print(variable_locale)


# fonction récursive
def recursive(a: int) -> None:
    print(a)
    a += 1
    if a == 5:
        recursive(a)


recursive(4) """


# fonction récursive pour calculer une factiorelle
def factoriel(a: int) -> int:
    if a > 1:
        return factoriel(a - 1) * a
    else:
        return a


print(factoriel(12))


def square_root(nb):
    return sqrt(nb)


print(square_root(9))
