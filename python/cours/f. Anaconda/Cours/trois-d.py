import matplotlib.pyplot as plt
import numpy as np

# Création de données en 3D
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Création du tracé 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracé du diagramme de dispersion en 3D
ax.scatter(x, y, z, c='blue', marker='o', label='Données 3D')

# Ajout de labels aux axes
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')

# Ajout d'une légende
ax.legend()

# Affichage du tracé 3D
plt.show()
