from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

import uvicorn
from fastapi import FastAPI, Body, Header, Cookie
from pydantic import BaseModel, Field


def create_app():
    lapp = FastAPI()

    @lapp.get('/items')
    async def read_items(dtrixviz_access_token: Optional[str] = Cookie(None, alias='dtrixviz-access-token')):
        return {
            'dtrixviz-access-token': dtrixviz_access_token
        }

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_cookie:app', host='0.0.0.0', port=8000, reload=True)
