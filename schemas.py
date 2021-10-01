from pydantic import BaseModel
from typing import Optional


class SignUp(BaseModel):
    id: Optional[int]
    name: str
    username: str
    email: str
    password: str
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'name': 'Example',
                'username': 'example',
                'email': 'example@gmail.com',
                'password': 'password',
                'is_active': True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='e51c0378d81d300da91ccef9e45af589c33e05eb42f287107952e39f0871e29c'


class LoginModel(BaseModel):
    username:str
    password:str

