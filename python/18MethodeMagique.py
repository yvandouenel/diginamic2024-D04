class User:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    # Surcharge, réécriture, polymorphisme
    def __str__(self):
        return f"Utilisateur : {self.prenom.capitalize()} {self.nom.upper()} "


johnny = User("Halliday", "johnny")
Milene = User("Farmer", "Milène")
print(johnny)
print(Milene)
print(vars(johnny))
