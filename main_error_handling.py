import uvicorn
from fastapi import FastAPI, HTTPException


items = {'foo': 'The Foo Wrestlers'}

def create_app():
    app = FastAPI()

    @app.post('/items/{item_id}')
    async def read_item(item_id: str):
        if item_id not in items:
            raise HTTPException(status_code=404, detail={'code': 'ERR_101', 'message': 'Item not found'})

        return {
            'item': items[item_id]
        }

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_error_handling:app', host='0.0.0.0', port=8000, reload=True)
