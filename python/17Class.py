# La majuscule indique par convention que User est une classe
""" class User:
    def __init__(self, firstname: str, lastname: str):
        # attributs ou propriétés des instances
        self.firstname = firstname
        self.lastname = lastname

    # Déclaration de la méthode "print_lastname" appelable depuis toutes les instances de User
    def print_lastname(self):
        print(f"Nom de famille : {self.lastname}")

    def introduce_my_self(self):
        print(f"Bonjour, je m'appelle {self.firstname} {self.lastname}")


# instanciations d'utilisateurs
user1 = User("Serge", "Lama")  # Appel de la méthode __init__
user2 = User("Robin", "Hotton")  # Appel de la méthode __init__

# appel de la méthode print_lastame
user1.print_lastname()
user2.print_lastname()

user1.introduce_my_self()


class Dog:
    # attribut de classe
    species = "Chien"
    paws = 4

    def __init__(self, name: str, age: int):
        # attributs d'instance
        self.name = name
        self.age = age

    def introduce_my_self(self):
        print(f"Waouf, je m'appelle {self.name} et je suis un {Dog.species}")
        print("self dans l'espace de la méthode introduce_my_self", vars(self))


# Instanciation
filou = Dog("Filou", 4)
zazi = Dog("Zazi", 12)

# Appel d'une méthode
filou.introduce_my_self()
zazi.introduce_my_self()
print("filou dans l'espace global", vars(filou)) """


class Dog:
    # Class attribute
    species = "Chien"
    # Class attribute to keep track of the number of Dog instances
    dogs_number = 0

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

        # Increment the class attribute each time a Dog is instantiated
        Dog.increment_dogs_number()

    @classmethod
    def increment_dogs_number(cls):
        cls.dogs_number += 1


# Instanciation de 2 chiens
filou = Dog("Filou", 4)
zazi = Dog("Zazi", 12)

# Affichage dans la console des attributs
print(filou.name)
print(filou.species)
print(filou.dogs_number)  # 2

print(zazi.name)
print(Dog.species)
print(Dog.dogs_number)  # 2
