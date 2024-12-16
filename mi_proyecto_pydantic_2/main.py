from datetime import datetime
from pydantic import BaseModel, validator
from fastapi import FastAPI
from typing import Optional
class User(BaseModel):
    id: int
    nombre: str = "Pepito Perez"
    fecha_hora: datetime | None = None  # Asegúrate de que la fecha se maneje como datetime
    valores: list[int] = []
# Datos externos con la fecha en formato correcto
external_data = {
    'id': 1001,
    'fecha_hora': '2024-12-06 08:42:00',  # Formato de fecha y hora correcto
    'valores': [1002, 1003, 1004]
}
# Crear el modelo User usando los datos externos
user = User(**external_data)
print(user)
print(user.id)
# Inicialización de FastAPI
app = FastAPI()
@app.get('/')
def index():
    return {'mensaje': 'Bienvenidos a la práctica de API'}
# Modelo de Item con validación de precio
class Item(BaseModel):
    nombre: str
    precio: float
    is_offer: bool = None
    @validator('precio')
    def precio_positivo(cls, v):
        if v <= 0:
            raise ValueError('Precio debe ser positivo')
        return v
@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}
# Modelo de usuario con validación de contraseñas
class Userpsw(BaseModel):
    username: str
    psw: str
    psw1: str
    
    @validator('psw1')
    def password_match(cls, v, values, **kwargs):
        if 'psw' in values and v != values['psw']:
            raise ValueError('Las contraseñas no coinciden')
        return v
@app.post("/users/")
async def create_user(user: Userpsw): 
    return {
        'username': user.username,
        'psw': user.psw,
        'psw1': user.psw1
    }
# Ejemplo de uso
user_data = {
    'username': 'usuario',
    'psw': 'contraseña',
    'psw1': 'contraseña'
}
user_with_password = Userpsw(**user_data)
print(user_with_password)