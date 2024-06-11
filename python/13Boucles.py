ma_liste = [1, 2, 3, 4]

for nb in ma_liste:
    print(nb + 2)  # Nous printons chaque chiffre dans ma_liste en ajoutant 2


ma_string = "python"

for char in ma_string:
    print(f"la lettre {char} !")

for x in range(5):
    print(x)


ma_liste = ["a", "b", "c", "d", "e"]
print(ma_liste[0])
for index, char in enumerate(ma_liste):
    print(f"la lettre {char} est à l'index {index}.")


ma_liste = [False, True, False, False, False]

for booleen in ma_liste:
    if booleen is True:
        print("élément vrai trouvé!")
        break
else:
    print("Tous les éléments de la liste sont faux.")

print("Après la boucle")

total = 20
x = 0

while x < total:
    print(x)
    x += 1

print("x après la boucle : ", x)

ma_liste = ["COUCOU", "PYTHON", "lowercase"]

# chaque fois qu'on croise une string en uppercase on passe à l'itération suivante sans exécuter le reste du code
for string in ma_liste:
    if string.isupper():
        continue
    print(string)  # nous ne printons que "lowercase"

ma_liste = [1, 2, 3, 4, 5]

for x in ma_liste:
    if x >= 4:
        print("C'en est trop pour moi, je m'en vais!")
        break  # sortie de boucle donc la ligne suivante ne sera jamais exécutée
    print(x)


ma_liste = [1, 2, 3, 4, 5]
liste_paire = []

for x in ma_liste:
    if x % 2 == 0:
        liste_paire.append(x * 2)

print(liste_paire)

ma_liste = [1, 2, 3, 4, 5]

liste_paire = [x * 2 for x in ma_liste if x % 2 == 0]

print(liste_paire)

any_false = any([True, True, True, False])
all_true = all([True, True, True])

print(any_false)  # True au moins une condition est False
print(all_true)  # True car toutes les conditions sont True

ma_liste = [1, 3, 5, 7, 9, 11, 13, 16]

print([x % 2 != 0 for x in ma_liste])
# Véririfie si tous les éléments sont impairs
print(all([x % 2 != 0 for x in ma_liste]))

notes = [8, 7, 12]

print([x >= 10 for x in notes])

if any(
    [x >= 10 for x in notes]
):  # on teste si au moins une valeur est supérieure ou égale à 10
    print(
        "Au moins une note est >= à 10"
    )  # Au moins une des notes est en dessous de 10
else:
    print("Toutes les notes sont  inférieures à 10")

""" any_false = any([False, True])  # au moins un qui est vrai
all_true = all([True, True])  # tous vrai

print("any_false : ", any_false)  # True au moins une condition est False
print("all_true :", all_true)  # True car toutes les conditions sont True """
