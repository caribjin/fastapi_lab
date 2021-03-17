from typing import Optional, Set, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
import uvicorn


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str = Field(..., title='Name Title', description='Name Description', min_length=1, max_length=10)
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


def create_app():
    lapp = FastAPI()

    @lapp.put('/items/{item_id')
    async def update_item(item_id: int, item: Item):
        result = {
            'item_id': item_id,
            'item': item
        }

        return result

    @lapp.post('/offers/')
    async def create_offer(offer: Offer):
        return offer

    @lapp.post('/index-weights/')
    async def create_index_weights(weights: Dict[str, float]):
        return weights

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main3:app', host='0.0.0.0', port=8000, reload=True)