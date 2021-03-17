import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            'example': {
                'name': 'Foo',
                'description': 'A very nice item',
                'price': 35.4,
                'tax': 3.2
            }
        }

def create_app():
    lapp = FastAPI()

    @lapp.put('/items/{item_id')
    async def update_item(item_id: int, item: Item):
        result = {
            'item_id': item_id,
            'item': item
        }

        return result

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main4:app', host='0.0.0.0', port=8000, reload=True)