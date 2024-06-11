liste_vide = []
liste_ints = [1, 2, 3, 4, 5]
liste_strings = ["coucou", "ca", "va", "?"]
liste_mix = [1, "Super", True, [1, 2, "Bonjour"]]

print(liste_ints[4])

ma_liste = [1, 2, 3]
ma_liste.append(4)

ma_liste.extend([5, 6, 7])
print(ma_liste)


ma_liste.remove(3)
ma_liste.pop(0)

print(ma_liste)

liste_mix[3].pop(2)
print(liste_mix)

ma_liste = [1, 2, 3, 4, 5, 6]

print(ma_liste[0])  # [1]

print(ma_liste[3:5])  # [4, 5] - exlusion de l'index 5
print(ma_liste[:2])  # [1, 2] - depuis le début jusqu'à l'index 2 exclu
print(
    ma_liste[2:-1]
)  # [3, 4, 5] - depuis l'index 2 jusqu'au dernier élément exclus (-1 représente le dernier élément)

print(ma_liste[::2])  # entièreté de la liste avec un pas de 2 (1 chiffre sur 2)
print(ma_liste[2:5:2])  # [3, 5] depuis l'index 2 jusqu'à l'index 5 avec un pas de 2
print(ma_liste[::-1])  # entièreté de la liste en sens inverse
print(ma_liste)  # entièreté de la liste

liste_str = ["a", "b", "z", "c", "r", "m", "y"]
print("liste_str avant sort", liste_str)
liste_int = [23, 1, 2, 75, 54, 2, 42]
liste_str_sorted = sorted(liste_str)  # fonction pure ou impure
liste_int.sort()

print("liste_str après sort", liste_str)
print(liste_str_sorted)  # ['a', 'b', 'c', 'm', 'r', 'y', 'z']
print(liste_int)  # [1, 2, 2, 23, 42, 54, 75]
print(",".join(liste_str_sorted))

test_string = "salut, tu vas,  bien?"
print(test_string.split(", "))
