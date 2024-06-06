**Objectif :** Mettre en pratique la création de tests unitaires pour les routes d'une application FastAPI.

Pour cet exercice, nous allons considérer une application FastAPI nommée `main` avec les routes suivantes :
- un get avec un retour fixé
- un get avec une condition sur l'id
- un post pour créer un item json

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/create_item")
def create_item(name: str, description: str):
    return {"name": name, "description": description}
```

**Instructions :**

1. Commencez par créer une classe de tests appelée `TestFastAPIRoutes` qui hérite de `unittest.TestCase`.

2. Utilisez la méthode `setUp` pour initialiser une instance de `TestClient` pour l'application FastAPI.

3. Écrivez un test unitaire (`test_route_hello_world`) pour la route `/hello` qui vérifie que la réponse a un code HTTP 200 et que le contenu de la réponse est un JSON avec la clé `"message"` égale à `"Hello, World!"`.

4. Ajoutez une deuxième classe de tests appelée `TestFastAPIWithDependencies` pour tester une route qui dépend d'une fonction externe (`get_db` dans cet exemple).

5. Écrivez un test unitaire (`test_route_with_dependency`) pour la route `/items/42` qui vérifie que la réponse a un code HTTP 200 et que le contenu de la réponse est un JSON avec la clé `"item_id"` égale à `42`.

6. Enfin, créez une troisième classe de tests appelée `TestFastAPIValidation` pour tester la validation des données pour une route qui reçoit des données en tant que modèle.

7. Écrivez un test unitaire (`test_model_validation`) pour la route `/create_item` qui vérifie que la réponse a un code HTTP 200 et que le contenu de la réponse est un JSON avec les données correctes (`{"name": "example", "description": "test"}`).

8. Exécutez le script pour vérifier que tous les tests passent avec succès.