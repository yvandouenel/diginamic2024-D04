**Objectif :** Mettre en pratique l'utilisation de mocks pour simuler une dépendance externe (comme une session de base de données) dans un test FastAPI.

**Instructions :**

1. Dans votre application FastAPI (`main.py`), créez une route supplémentaire `/items/{item_id}/details` qui renvoie des détails détaillés pour un item en fonction de son ID.

   ```python
   from fastapi import Depends, HTTPException

   @app.get("/items/{item_id}/details")
   def read_item_details(item_id: int, db: Session = Depends(get_db)):
       item = get_item_from_db(db, item_id)
       if item is None:
           raise HTTPException(status_code=404, detail="Item not found")
       return {"item_id": item_id, "details": f"Details for item {item_id}"}
   ```

   N'oubliez pas de mettre à jour vos dépendances, importations, et fonction `get_item_from_db` pour prendre en charge cette nouvelle route.

2. Écrivez une fonction de test appelée `test_read_item_details_with_mock_db` dans le même fichier de tests que les exercices précédents. Utilisez `patch` pour remplacer la vraie dépendance (`get_db`) par un mock (`mock_db`).

3. Utilisez `TestClient` pour simuler une requête HTTP vers la nouvelle route `/items/{item_id}/details`. Assurez-vous de tester un `item_id` valide.

4. Utilisez des assertions pour vérifier que la réponse a le bon code HTTP et que le contenu de la réponse est correct.

5. Ajoutez une assertion pour vérifier que la dépendance simulée (`mock_db`) a été appelée exactement une fois.

6. Exécutez le script de test pour vous assurer que le test `test_read_item_details_with_mock_db` passe avec succès.