age = 17
if age > 18:  # sera évaluée False
    print("vétéran")
elif age == 18:  # sera évaluée True
    print("tout juste majeur")
else:  # ne sera jamais évaluée
    print("mineur")

print("majeur") if age >= 18 else print("mineur")

nom = "Gérard"

cond_xor = ("x" not in nom) ^ ("d" not in nom)

if cond_xor:
    print("condition vraie")
else:
    print("condition fausse")
