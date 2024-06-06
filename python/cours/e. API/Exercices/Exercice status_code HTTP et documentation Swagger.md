Voici le début du code de l'exercice. Les schémas serviront pour les entrés et sortis d'information par les routes.

fake_db est une liste de dictionnaire et servira de pseudo base de donnée pour l'exercice. On pourra y ajouter, modifier et supprimer des Items.

```python
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException

# Création de l'application FastAPI
app = FastAPI()

# Schémas Pydantic pour la validation des données
class ItemCreate(BaseModel):
    name: str

class ItemUpdate(BaseModel):
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str

# Simulons une pseudo base de données avec un tableau de dictionnaires
fake_db: List[ItemResponse] = []
```

> [!INFO] Documentation
> N'oubliez pas la documentation avec le docstring et le summary.
> Les autres type de documentations seront demandé dans les questions.

1. **Création d'un item**
	- Créez une route POST à l'endpoint "/item" qui permet de créer un nouvel item.
	- Utilisez un modèle Pydantic appelé `ItemCreate` avec un champ `name` de type chaîne de caractères.
	- La route devrait renvoyer l'item créé avec un code de statut 201 (HTTP_201_CREATED).
	- Utilisez le modèle Pydantic `ItemResponse` pour spécifier la structure de la réponse.

2. **Lecture des items**
	- Créez une route GET à l'endpoint "/item" qui renvoie la liste des items.
	- Utilisez un modèle Pydantic appelé `ItemResponse` pour spécifier la structure des items.
	- Ajoutez un tag "items" à la route pour la documentation Swagger.

> [!TIP] vérifier son code
> Maintenant que vous avec fait un create et un read. Pensez à utiliser Swagger pour verifier que votre code fonctionne.

3. **Mise à jour d'un item (PUT)**
	- Créez une route PUT à l'endpoint "/item/{item_id}" pour mettre à jour un item existant.
	- Utilisez un modèle Pydantic appelé `ItemUpdate` avec un champ `name` de type chaîne de caractères.
	- La route devrait renvoyer l'item mis à jour avec son ID et son nom.
	- Utilisez le modèle Pydantic `ItemResponse` pour spécifier la structure de la réponse.
	- Assurez-vous de gérer les cas où l'item n'est pas trouvé.

4. **Mise à jour d'un item (PATCH)**
	-  Créez une route PATCH  à l'endpoint "/item/{item_id}"
	- on gardera les même conditions que celles du PUT

5. **Suppression d'un item**
	- Créez une route DELETE à l'endpoint "/item/{item_id}" pour supprimer un item en fonction de son ID.
	- La route devrait renvoyer un message indiquant que l'item a été supprimé avec succès.
	- Renvoyez un json pour spécifier que l'objet a bien été supprimé
	- Assurez-vous de gérer les cas où l'item n'est pas trouvé.

[[Correction status_code HTTP et documentation Swagger]]