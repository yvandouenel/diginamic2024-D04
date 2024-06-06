simple_quote = (
    "Avec une simple quote, je ne peux pas passer à la ligne \n sauf à échapper n..."
)


double_quote = """Je suis une chaine  
mais je peux m'étendre sur plusieurs lignes"""


simple_quote_triple = """Même chose, et le truc cool
c'est que je n'ai plus besoin
d'échapper les apostrophes!"""

print(simple_quote)
print(double_quote)
print(simple_quote_triple)
print("passement\bde ligne!")

raw_string = r"Je suis une raw string,\nsans passage à la ligne!"

print(raw_string)

path = "C:\\User\\Bob"
pathraw = r"C:\User\Bob"
print(path)
print(pathraw)
