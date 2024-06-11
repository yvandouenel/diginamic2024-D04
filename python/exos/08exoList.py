# Printer le nombre 5 à partir de la liste suivante
liste = [1, 2, [3, 4, [5, 6, 7]]]

print(liste[2][2][0])
print(liste[2][:2])

texte = "Les Cucurbitaceae (Cucurbitacées) sont une famille de plantes dicotylédones de l'ordre des Cucurbitales, originaires pour la plupart des régions tropicales et subtropicales, qui comprend environ 800 espèces réparties en 180 genres. Ce sont généralement des plantes herbacées, annuelles ou vivaces, à port rampant ou grimpant, aux tiges munies de vrilles, et plus rarement des arbustes. Ces plantes sont sensibles au gel. Les fleurs sont unisexuées, portées parfois par les mêmes plantes (monoïques), parfois par des plantes différentes (dioïques). Les fruits sont le plus souvent des baies modifiées appelées péponides, plus rarement des fruits secs (capsules, samares). De nombreuses espèces sont cultivées pour leur fruits comestibles (courges, courgettes, concombres, cornichons, doubeurres, melons, pastèques, chayotes, etc.) et parfois pour leurs graines (courge à huile, pistache africaine). Leur domestication est très ancienne et remonte à plusieurs milliers d'années, tant dans le Nouveau Monde (Cucurbita, Sechium) que dans l'Ancien (Citrullus, Cucumis, Lagenaria, Luffa, Albanus Quénetus)."

list_texte = texte.split(". ")
list_texte_inverse = list_texte[::-1]
# print(list_texte)
# print(list_texte_inverse)
join = "\\".join(list_texte_inverse)
print(join)
