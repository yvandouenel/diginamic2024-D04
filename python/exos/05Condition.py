mot = input("Entrez un mot ")
if "a" in mot.lower() or "e" in mot.lower():
    print("beep")

if ("a" in mot.lower()) ^ ("e" in mot.lower()):
    print("boop")
