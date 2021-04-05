import uvicorn
from fastapi import FastAPI, File, UploadFile


def create_app():
    app = FastAPI()

    from typing import List
    @app.post('/files/')
    async def create_file(files: List[bytes] = File(...)):
        return {
            'file_size': [len(file) for file in files]
        }

    @app.post('/uploadfile/')
    async def create_upload_file(files: List[UploadFile] = File(...)):
        return {
            'filename': [file.filename for file in files]
        }

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run('main_file:app', host='0.0.0.0', port=8000, reload=True)
