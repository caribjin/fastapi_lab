from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float]
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    repeat_at: Optional[time] = None
    process_after: Optional[timedelta] = None


def create_app():
    lapp = FastAPI()

    @lapp.put('/items/{item_id}')
    async def update_item(
            item_id: UUID,
            item: Item
    ):
        result = {
            'item_id': item_id,
            'item': item
        }

        return result

    @lapp.put('/items2/{item_id')
    async def update_item2(
            item_id: UUID,
            start_datetime: Optional[datetime] = Body(None),
            end_datetime: Optional[datetime] = Body(None),
            repeat_at: Optional[time] = Body(None),
            process_after: Optional[timedelta] = Body(None)
    ):
        start_process = start_datetime + process_after
        duration = end_datetime - start_process

        return {
            "item_id": item_id,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "repeat_at": repeat_at,
            "process_after": process_after,
            "start_process": start_process,
            "duration": duration,
        }

    return lapp


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_extra_types:app', host='0.0.0.0', port=8000, reload=True)
