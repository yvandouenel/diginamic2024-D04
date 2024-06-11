# ressemble à un tuple mais en plus strict car un tuple accepte des valeurs non primitives
mon_set = {"mon", "super", "set"}

test_tuple = (1, 2, 3, 1)
# créer un set à partir d'un tuple
duplicats_interdit = set(test_tuple)
print(duplicats_interdit)  # {1, 2, 3}
