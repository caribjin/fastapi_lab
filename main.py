from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

from app.common.config import conf


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()

    # 데이터 베이스 초기화
    class Item(BaseModel):
        id: int
        name: str
        price: float = 50000
        is_offer: Optional[bool] = None

    my_item: Item = Item(id=1, name='test', price=1000, is_offer=False)

    # print(f'name={my_item.name} price={my_item.price} is_offer={my_item.is_offer}')

    my_item2: Item = Item(**{
        'id': 2,
        'name': 'test2',
        # 'price': 3000,
        'is_offer': True
    })

    # print(f'name={my_item2.name} price={my_item2.price} is_offer={my_item2.is_offer}')

    # 레디스 초기화

    # 미들웨어 정의

    # 라우터 정의

    @app.get('/')
    def read_root():
        return {'Hello': 'World'}

    @app.get('/items/{item_id}')
    def read_item(item_id: int, q: Optional[str] = None):
        return {'item_id': item_id, 'q': q}

    @app.post('/items/{item_id}')
    def update_item(item_id: int, item: Item):
        return {'item_id': item_id, 'item_name': item.name}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
