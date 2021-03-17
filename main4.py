import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(..., example='Foo')
    description: Optional[str] = Field(None, example='A very nice item')
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(..., example=3.2)

    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'name': 'Foo',
    #             'description': 'A very nice item',
    #             'price': 35.4,
    #             'tax': 3.2
    #         }
    #     }

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