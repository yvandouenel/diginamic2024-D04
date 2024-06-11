string_immuable = "coucou ca va ?"
string_upper = string_immuable.upper()
print(string_immuable)
print(string_upper)

liste_muable = [1, 4, 3, 2]
liste_muable.sort()

print(liste_muable)

mon_tuple = (1, 2, 3)
mon_tuple_mix = ("coucou", True, 45, ["hello", 2, 3])

tubple_titres = ("nom", "prenom", "email")

# On peut convertir un tuple en une liste avec la fonction list(), et inversement avec la fonction tuple()
# print(list(mon_tuple))

# On ne peut certes pas modifier un tuple mais on peut modifier les objets muables qui appartiennent au tuple
mon_tuple_mix[3][0] = "42"  # Pour rappel une liste est un objet muable
