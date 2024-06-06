```python
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

from main import app, get_db, get_item_from_db

def test_read_item_details_with_mock_db():
    # Création d'un mock de la dépendance (session de base de données)
    mock_db = Mock()

    # Utilisation de patch pour substituer la vraie dépendance par le mock
    with patch("main.get_db", return_value=mock_db):
        # Utilisation de TestClient pour simuler une requête HTTP
        with TestClient(app) as client:
            # Appel de la nouvelle route avec un item_id spécifié
            response = client.get("/items/42/details")

    # Assertion sur le résultat
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "details": "Details for item 42"}

    # Assertion sur l'utilisation de la dépendance simulée
    mock_db.assert_called_once()  # Vérifie si la dépendance a été appelée exactement une fois
    # Vous pouvez également ajouter d'autres assertions en fonction de ce que vous voulez vérifier sur l'utilisation du mock

if __name__ == '__main__':
    unittest.main()
```