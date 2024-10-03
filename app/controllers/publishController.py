from fastapi import APIRouter
from app.models.message import MessagePBF, MessageGCP
from app.services.publishService import pub_message

router = APIRouter()

@router.post("/publish/pbf")
async def read_pub_massage(message: MessagePBF):
    result = await pub_message(message, "sample-pbf") #Please change the name before prod
    return result

@router.post("/publish/gcp")
async def read_pub_massage(message: MessageGCP):
    result = await pub_message(message, "sample-gcp") #Please change the name before prod
    return result