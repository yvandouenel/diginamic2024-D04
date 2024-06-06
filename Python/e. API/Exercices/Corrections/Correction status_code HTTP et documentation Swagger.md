```python
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException

class ItemCreate(BaseModel):
    name: str

class ItemUpdate(BaseModel):
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str

# Simulons une pseudo base de données avec un tableau de dictionnaires
fake_db: List[ItemResponse] = []

# 1. Création d'un item
@app.post("/item", response_model=ItemResponse, status_code=201, tags=["items"])
async def create_item(item_create: ItemCreate):
    # Générez l'ID de manière fictive (en utilisant la taille actuelle du tableau + 1)
    item_id = len(fake_db) + 1
    item = ItemResponse(id=item_id, **item_create.dict())
    fake_db.append(item)
    return item

# 2. Lecture des items
@app.get("/item", response_model=List[ItemResponse], tags=["items"])
async def read_items():
    return fake_db

# 3. Mise à jour d'un item (PUT)
@app.put("/item/{item_id}", response_model=ItemResponse, tags=["items"])
async def update_item(item_id: int, item_update: ItemUpdate):
    for item in fake_db:
        if item.id == item_id:
            updated_item = ItemResponse(id=item_id, **item_update.dict())
            fake_db[fake_db.index(item)] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# 4. Mise à jour d'un item (PATCH)
@app.patch("/item/{item_id}", response_model=ItemResponse, tags=["items"])
async def update_item(item_id: int, item_update: ItemUpdate):
	pass

# 5. Suppression d'un item
@app.delete("/item/{item_id}", response_model=dict, tags=["items"])
async def delete_item(item_id: int):
    for item in fake_db:
        if item.id == item_id:
            fake_db.remove(item)
            return {"message": "Item successfully deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

```