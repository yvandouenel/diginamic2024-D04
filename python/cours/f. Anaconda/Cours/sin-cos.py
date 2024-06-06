import matplotlib.pyplot as plt
import numpy as np

# Données
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Création de la figure et des sous-tracés
fig, ax = plt.subplots()

# Premier graphique (en bleu)
ax.plot(x, y1, label='Sin(x)', color='blue')

# Deuxième graphique (en rouge)
ax.plot(x, y2, label='Cos(x)', color='red')

# Titre du sous-tracé
ax.set_title('Graphiques de Sin(x) et Cos(x)')

# Légende
ax.legend()

# Affichage du sous-tracé

######################################################################
######################################################################
######################################################################

# Données
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Création de la figure et des sous-tracés
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 4))

# Premier sous-tracé (à gauche)
axes[0][0].plot(x, y1, color='blue', label='Sin(x)')
axes[0][0].set_title('Graphique de sin(x)')
axes[0][0].legend()

# Deuxième sous-tracé (à droite)
axes[1][2].plot(x, y2, color='green', label='Cos(x)')
axes[1][2].set_title('Graphique de cos(x)')
axes[1][2].legend()

# Réglages supplémentaires (optionnels)
plt.suptitle('Graphiques de Sin(x) et Cos(x)')
plt.show()