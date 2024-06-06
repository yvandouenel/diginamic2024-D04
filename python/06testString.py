minuscule = "minuscule"
# majuscule va stocker le résultat de upper et ne modifiera pas la valeur de minuscule
# car c'est une méthode pure
majuscule = minuscule.upper()

print(minuscule)  # "minuscule"
print(majuscule)  # "MINUSCULE"


crier = "PAS LA PEINE DE CRIER !"
# lower ne va pas modifier crier (car c'est une fonction pure)
# mais va permettre de stocker des minuscules
parler = crier.lower()

print(parler)  # "pas la peine de crier!"
print(crier)
