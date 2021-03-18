from typing import Optional, Set, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl, EmailStr
import uvicorn


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = 10.5
    tags: List[str] = []


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


items = {
    "foo": {"name": "Foo", "price": 10.0},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": ['a', 'b', 'c']},
}


def create_app():
    lapp = FastAPI()

    @lapp.post('/items/', response_model=Item)
    async def create_item(item: Item):
        return item

    @lapp.post('/user/', response_model=UserOut)
    async def create_user(user: UserIn):
        return user

    @lapp.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
    async def read_item(item_id: str):
        return items[item_id]

    @lapp.get('/items/{item_id}/name', response_model=Item, response_model_include={'name', 'description'})
    async def read_item_name(item_id: str):
        return items[item_id]

    @lapp.get('/items/{item_id}/public', response_model=Item, response_model_exclude={'tax'})
    async def read_item_public(item_id: str):
        return items[item_id]

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_response_model:app', host='0.0.0.0', port=8000, reload=True)