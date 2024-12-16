from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    name:str
    edad:int
    email:EmailStr

user_data={
    "name":"Cesar",
    "edad":26,
    "email":"cesar@gmail.com"
}

invalid_user_data={
    "name":"Cesar",
    "edad":0,
    "email":"cesar@gmail.com"
}

try:
    user_invalid=User(**invalid_user_data)
except ValidationError as e:
    print("error de validacion: ", e.json())

user=User(**user_data)
print(user)