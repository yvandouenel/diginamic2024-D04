class User:
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom

    def get_full_name(self):
        print(f"Utilisateur {self.nom.upper()} {self.prenom.capitalize()}")


class Admin(User):
    def __init__(self, nom: str, prenom: str):
        super().__init__(nom, prenom)
        self.admin = True

    # Surcharge de la méthode de la classe mère
    def get_full_name(self):
        print(f"Administrateur {self.nom.upper()} {self.prenom.capitalize()}")


user = User("Brassens", "Georges")
admin = Admin("Clooney", "Georges")
user.get_full_name()  #
admin.get_full_name()  # "Administrateur CLOONEY Georges"
