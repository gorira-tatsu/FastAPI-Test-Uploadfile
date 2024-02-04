from typing import Annotated
import io

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    with open('test.txt', 'wb') as write_file:
        write_file.write(contents)