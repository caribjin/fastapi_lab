from typing import Optional, List, Set

import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Optional[str] = 'This is item description'
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    sets: Set[str] = set()


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


def create_app():
    result_app = FastAPI()

    @result_app.post('/items/')
    async def create_item(item: Item):
        item_dict = item.dict()

        if item.tax:
            price_with_tax = item.price + item.tax
            item_dict.update({
                "price_with_tax": price_with_tax
            })

        return item_dict

    @result_app.put('/items/{item_id}')
    async def update_item(
            *,
            item_id: int = Path(..., title='The ID of the item to get', ge=0, le=1000),
            item: Optional[Item] = None,
            user: Optional[User] = None,
            q: Optional[str] = None
    ):
        result = {
            'item_id': item_id,
            **item.dict(),
            **user.dict()
        }

        if q:
            result.update({'q': q})

        if item.tax:
            price_with_tax = item.price + item.tax
            result.update({
                'price_with_tax': price_with_tax
            })

        return result

    @result_app.get('/items')
    async def read_items(q: Optional[str] = Query(
        None,
        title='Query String',
        description='아이템을 위한 쿼리 스트링',
        min_length=3,
        alias='item-query'
    ), q2: Optional[str] = Query(
        None,
        description='대체 쿼리',
        deprecated=True
    )):
        result = {
            'q': q,
            'q2': q2
        }

        return result

    return result_app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main2:app', host='0.0.0.0', port=8000, reload=True)
