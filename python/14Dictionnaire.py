from datetime import date

# []  - liste
# () - tuple
# {} - dictionnaire

mon_dict = {
    "nom": "Bouchard",
    "prenom": "Gérard",
    "admin": True,
    "date_naissance": date(1982, 5, 26),
    "nombre_abonnes": 123627,
    "enfants": [{"nom": "Bouchard", "prenom": "Timothée"}],
}

print(mon_dict.get("admin"))  # True
print(mon_dict["enfants"][0]["prenom"])  # Timothée

test = mon_dict.get("truc", "valeur par défaut")
print(test)
mon_dict = {"a": True, "b": True, "c": False}

mon_dict["a"] = False

print(mon_dict)

mon_dict = {"test": [1, 2, 3], "dev": [4, 5, 6]}

mon_dict["prod"] = [7, 8, 9]

print(mon_dict)

mon_dict = {
    1: {"nom": "Chahiri", "prenom": "Hamza"},
    2: {"nom": "Martin", "prenom": "Etienne"},
}

if 2 in mon_dict:  # contrôler la présence de la clé pour éviter de soulever une erreur
    del mon_dict[2]

print(mon_dict)

mon_dict = {"a": True, "b": True, "c": False}

for item in mon_dict.items():
    print(item)

for key, value in mon_dict.items():
    print(f"la clé {key} a pour valeur {value}")

mon_dict = {"a": True, "b": True, "c": False}

for item in mon_dict.items():
    print(item)

for key in mon_dict:
    print(f"la clé {key} a pour valeur {mon_dict.get(key, "message par défaut")}")
    print(f"la clé {key + "test"} a pour valeur {mon_dict.get(key + "test", "message par défaut")}")

