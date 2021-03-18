from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

import uvicorn
from fastapi import FastAPI, Body, Header
from pydantic import BaseModel, Field


def create_app():
    lapp = FastAPI()

    @lapp.get('/items')
    async def read_items(user_agent: Optional[str] = Header(None)):
        return {
            'User-Agent': user_agent
        }

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_header:app', host='0.0.0.0', port=8000, reload=True)
