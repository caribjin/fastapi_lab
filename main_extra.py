from typing import Optional, Union, List, Dict

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


class BaseItem(BaseModel):
    type: str
    description: str


class CarItem(BaseItem):
    type = 'car'


class PlainItem(BaseItem):
    type = 'plane'
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car"
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

items2 = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


class Item(BaseModel):
    name: str
    description: str


def fake_password_hasher(raw_password: str):
    return 'supersecret' + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print('user saved! ..not really')
    return user_in_db


def create_app():
    app = FastAPI()

    @app.post('/user/', response_model=UserOut)
    async def create_user(user_in: UserIn):
        user_saved = fake_save_user(user_in)
        return user_saved

    @app.get('/items/{item_id}', response_model=Union[PlainItem, CarItem])
    async def read_item(item_id: str):
        return items[item_id]

    @app.get('/items/', response_model=List[Item], status_code=status.HTTP_200_OK)
    async def read_items():
        return items2

    @app.get('/keyword-weights/', response_model=Dict[str, float])
    async def read_keyword_weights():
        return {'foo': 2.3, 'bar': 3.4}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_extra:app', host='0.0.0.0', port=8000, reload=True)
