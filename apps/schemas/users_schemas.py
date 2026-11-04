from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field( min_length = 4, max_length = 50, description = "Nome do usuário")
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    password: str = Field( min_length = 6, max_length = 15, description = "Senha do usuário")
    adress: Optional[str] = None
    img: Optional[str] = None


class UserLoginSchemas(BaseModel):
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    password: str = Field( min_length = 6, max_length = 15, description = "Senha do usuário")


class UserUpdateSchemas(BaseModel):
    name: str = Field( min_length = 4, max_length = 50, description = "Nome do usuário")
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    adress: Optional[str] = None
    img: Optional[str] = None


class UserPasswordUpdateSchemas(BaseModel):
    password: str
    new_password: str = Field( min_length = 6, max_length = 15, description = "Nova senha do usuário")


class UserResponseSchemas(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id_user: int
    name: str
    email: EmailStr
    type: str
    adress: Optional[str] = None
    img: Optional[str] = None
    created_at: datetime
