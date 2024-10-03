from pydantic import BaseModel
from datetime import date

class MessageBodyPBF(BaseModel):
    idapp: int
    name: str
    pin: int
    event: str

class MessagePBF(BaseModel):
    subject: str
    data: MessageBodyPBF
    
class MessageBodyGCP(BaseModel):
    idapp: int
    name: str
    date: str
    event: str #get in - get out - wrong pin - windows not available
    
class MessageGCP(BaseModel):
    subject: str
    data: MessageBodyGCP
