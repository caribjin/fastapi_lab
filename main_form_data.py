from typing import Optional, Union, List, Dict

import uvicorn
from fastapi import FastAPI, status, Form
from pydantic import BaseModel, EmailStr


def create_app():
    app = FastAPI()

    @app.post('/login/')
    async def login(username: str = Form(...), password = Form(...)):
        return {'username': username, 'password': password}

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_form_data:app', host='0.0.0.0', port=8000, reload=True)
