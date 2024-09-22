from pydantic import BaseModel

class Message(BaseModel):
    id: int
    name: str
    pin: int

class Message(BaseModel):
    subject: str
    data: Message