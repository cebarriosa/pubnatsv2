from fastapi import APIRouter
from app.models.message import Message
from app.services.publishService import pub_message

router = APIRouter()

@router.post("/publish")
async def read_pub_massage(message: Message):
    result = await pub_message(message)
    return result