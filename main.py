from typing import Optional
from fastapi import FastAPI
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

    # 레디스 초기화

    # 미들웨어 정의

    # 라우터 정의

    @app.get('/')
    def read_root():
        return {'Hello': 'World'}

    @app.get('/items/{item_id}')
    def read_item(item_id: int, q: Optional[str] = None):
        return {'item_id': item_id, 'q': q}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
