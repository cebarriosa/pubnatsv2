import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout
import json 
import nats
from nats.errors import TimeoutError
from fastapi import HTTPException

async def pub_message(message):
    
    nc = await nats.connect("nats://localhost:4222")
    # Create JetStream context.
    js = nc.jetstream()
    
    
    subject =  message.subject
    data = json.dumps(message.data.dict()).encode()
    
    await js.add_stream(name="sample-pbf", subjects=[subject])    
    try:  
        await js.publish(subject, data)

        return { "subject": subject, "data": message.data, "message": "message published"}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    