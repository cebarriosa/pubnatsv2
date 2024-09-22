from typing import Union

from fastapi import FastAPI
from app.controllers import publishController 

app = FastAPI()
app.include_router(publishController.router)

@app.get("/")
def read_root():
    return {"message": "Softwavecodes API"}

