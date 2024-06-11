liste = ["bernard", "gérard", "gontran", "jacqueline", "intrus", "nadia", "jack"]

for name in liste:
    if name == "intrus":
        print(name + " trouvé")
        break

liste_somme = [12.3, 34, 1, 0.4, 23, -17, 76, -300.2]
somme = 0
for x in liste_somme:
    somme += x

print(f"La somme de la liste est {somme}")

# A l'aide d'une boucle et d'une range, calculer le factoriel de 10 (3628800)
# Le factoriel d'un entier n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n
# Printer le résultat
fac = 1
for nb in range(1, 11):
    fac = fac * nb

print(fac)

# A l'aide d'une boucle while, demander à l'utilisateur de "Taper oui, ou non.", et tant que ce dernier n'a pas tapé "non", continuer de lui demander "Taper oui, ou non."

# Si dans un deuxième temps l'utilisateur ne tape ni "oui", ni "non", continuer la boucle en lui mettant un message d'erreur car l'input est invalide

""" reponse = input("Taper oui, ou non. ")
while reponse != "non":
    reponse = input("Taper oui, ou non. ")
    if reponse != "oui" and reponse != "non":
        print("erreur, veuillet entrer oui ou non")
"""
ma_liste = ["a", 3, True, "coucou", "r", 3.14, [1, 2, 3]]

for index, value in enumerate(ma_liste):
    print(f"L'élément à l'index {index} a pour valeur {value}")

# A l'aide d'une compréhension de liste générer une nouvelle liste suivant les règles suivante :
# Si le chiffre est un multiple de 5, le multiplier par 2
# Sinon, retourner sa division entière par 3
# Printer la nouvelle liste obtenue

liste_de_base = [23, 1, 27, 28, 3, 4, 763, 12, 90]

liste_result = [x * 2 if x % 5 == 0 else x // 3 for x in liste_de_base]

print(liste_result)

# A l'aide de boucles imbriquées, créer une nouvelle liste "flat", qui sera une liste applatie de "liste", ayant les éléments classés dans l'ordre décroissant : [7, 6, 5, 4, 3, 2, 1]
# [5, 2]
liste = [1, 3, 7, [4, 6, [5, 2]]]
flat = []
for elt in liste:
    # teste si l'élément est une liste
    if isinstance(elt, list):
        print("elt et une liste")
        for elt_child in elt:
            if isinstance(elt_child, list):
                for elt_child_child in elt_child:
                    flat.append(elt_child_child)
            else:
                flat.append(elt_child)
    else:
        flat.append(elt)
flat.sort(reverse=True)
print(flat)
