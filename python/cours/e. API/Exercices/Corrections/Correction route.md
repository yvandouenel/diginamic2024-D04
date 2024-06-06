```python
from fastapi import FastAPI

app = FastAPI()

# Partie 1 - Routes Get
@app.get("/clients")
def get_clients():
    return {"clients": "plein de clients"}

@app.get("/clients/{client_id}")
def get_client_by_id(client_id: int):
    return {"client": client_id}


# Partie 2 - Utiliser une pseudo BDD en JSON
fake_client_db = [
    {"nom": "hotton", "prenom": "robin"},
    {"nom": "hadjaz", "prenom": "benjamin"},
    {"nom": "helleu", "prenom": "gilles"},
    {"nom": "Vialla de soleyrol", "prenom": "damien"}
]

@app.get("/clients")
def get_clients():
    return {"clients": fake_client_db}

@app.get("/clients/{client_id}")
def get_client_by_id(client_id: int):
    if 0 <= client_id < len(fake_client_db):
        return {"client": fake_client_db[client_id]}
    else:
        return {"message": "Client not found"}

# Partie 3 - Paramètres optionnels (index_debut, nb_elements)
# J'ai changé la route afin qu'il n'y ai pas de conflit avec le premier get
@app.get("/clients/details")
def get_clients_details(index_debut: int = 0, nb_elements: int = None):
    if 0 <= index_debut < len(fake_client_db):
        end_index = len(fake_client_db) if nb_elements is None else index_debut + nb_elements
        return {"clients": fake_client_db[index_debut:end_index]}
    else:
        return {"message": "Invalid index_debut"}
```