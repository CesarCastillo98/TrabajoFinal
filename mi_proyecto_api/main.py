from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")

def hola_mundo():
    return {"Hola":"Mundo"}

@app.get("/usuarios/{usuario_id}")

def get_usuario(usuario_id:int, q:Optional[str] = None):
    return {"usuario_id":usuario_id,"q":q}
