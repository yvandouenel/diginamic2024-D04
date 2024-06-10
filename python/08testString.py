from datetime import date

x = 2
y = 3

# va nous donner le résultat "L'addition de 2 et 3 est égale à 5"
# Interpolation et concaténation
print(f"L'addition de {x} et {y} est égale à {x + y}")


print(
    "L'addition de {premier} et {second} est égale à {addition}".format(
        premier=x, second=y, addition=x + y
    )
)
z = 2

formatage = f"formatage de {z:04d} pour être sûr qu'il est composé de 4 chiffres"
print(formatage)

date_us = date(2022, 12, 24)  # création d'un object date

date_fr = f"Avec des slashs, c'est quand même plus lisible : {date_us:%d/%m/%Y}"

print(date_fr)

flute_a_bec = """
Souvent moquée et montrée du doigt, la flûte à bec est généralement mise de côté 
quand il s’agit d’être choisie quand on veut commencer un instrument. 
Jugée trop simple, petite, pas Rock’n Roll, et surtout associée aux cours 
de musique à l’école, la flûte n’a pas bonne réputation.
"""

print(f"{flute_a_bec:.10}")  # n'affichera que les 10 premiers caractères

age = 12

concat = "Bonjour j'ai %d ans" % age
print(concat)  # sera casté en integer

concat = "Bonjour j'ai %f ans" % age
print(concat)  # sera casté en float


print("Je concatene " + str(x) + " et " + str(y) + " avec +, quel plaisir.")
