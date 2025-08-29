from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Dummy database with more products
artisans = [
    {"id": 1, "name": "Kanchipuram Silk Saree", "location": "Tamil Nadu"},
    {"id": 2, "name": "Pashmina Shawl", "location": "Kashmir"},
    {"id": 3, "name": "Terracotta Pottery", "location": "West Bengal"},
    {"id": 4, "name": "Brass Lamp", "location": "Rajasthan"},
    {"id": 5, "name": "Handwoven Basket", "location": "Kerala"},
    {"id": 6, "name": "Wooden Toy Elephant", "location": "Tamil Nadu"},
    {"id": 7, "name": "Embroidered Scarf", "location": "Kashmir"},
    {"id": 8, "name": "Organic Soap Set", "location": "Himachal Pradesh"}
]

# Remove duplicates based on 'name' and 'location'
seen = set()
unique_artisans = []
for a in artisans:
    key = (a["name"], a["location"])
    if key not in seen:
        seen.add(key)
        unique_artisans.append(a)

# Reassign cleaned list with sequential IDs
for idx, a in enumerate(unique_artisans, start=1):
    a["id"] = idx

artisans = unique_artisans

# Pydantic models
class ArtisanItem(BaseModel):
    name: str
    location: str

class StoryRequest(BaseModel):
    product_name: str

# GET: fetch items
@router.get("/items")
def get_items():
    return artisans

# POST: add item
@router.post("/add_item")
def add_item(item: ArtisanItem):
    new_id = len(artisans) + 1
    new_item = {"id": new_id, "name": item.name, "location": item.location}
    artisans.append(new_item)
    return {"message": "Item added successfully ✅", "item": new_item}

# POST: generate story (enhanced dummy AI)
@router.post("/generate_story")
def generate_story(request: StoryRequest):
    # Generate a richer, more engaging story
    story = (
        f"Behold the {request.product_name}, a remarkable creation crafted with love and dedication. "
        f"Each piece carries the legacy of skilled artisans, reflecting the traditions and culture of India. "
        f"The materials are carefully chosen, and every detail is meticulously made to perfection. "
        f"Owning this product is not just about style; it’s about embracing a story, a heritage, and the passion of generations."
    )
    return {"product": request.product_name, "story": story}
