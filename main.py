from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
import auth 
from text_generation import Client

app = FastAPI()

client = Client("http://127.0.0.1:8080")

@app.get("/generate")
async def info(query: str,  max_token: int = 50, username: APIKey = Depends(auth.get_username)):
    output = client.generate(query, max_new_tokens=max_token).generated_text
    return output
