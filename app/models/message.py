from pydantic import BaseModel

class Message(BaseModel):
    idapp: int
    name: str
    pin: int
    event: str

class Message(BaseModel):
    subject: str
    data: Message
