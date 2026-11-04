from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
# ==================================================================================
# Create User Create
# ==================================================================================
class UserCreate(BaseModel):
    name: str = Field( min_length = 4, max_length = 50, description = "Nome do usuário")
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    password: str = Field( min_length = 6, max_length = 15, description = "Senha do usuário")
    adress: Optional[str] = None
    img: Optional[str] = None


# ==================================================================================
# Create User Login
# ==================================================================================

class UserLoginSchemas(BaseModel):
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    password: str = Field( min_length = 6, max_length = 15, description = "Senha do usuário")


# ==================================================================================
# Create User Update
# ==================================================================================

class UserUpdateSchemas(BaseModel):
    name: str = Field( min_length = 4, max_length = 50, description = "Nome do usuário")
    email: EmailStr = Field( min_length = 1, max_length = 100, description = "Email do usuário")
    adress: Optional[str] = None
    img: Optional[str] = None

# ==================================================================================
# Create User Password Update
# ==================================================================================
class UserPasswordUpdateSchemas(BaseModel):
    password: str
    new_password: str = Field( min_length = 6, max_length = 15, description = "Nova senha do usuário")

# ==================================================================================
# Create User Response
# ==================================================================================
class UserResponseSchemas(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id_user: int
    name: str
    email: EmailStr
    type: str
    adress: Optional[str] = None
    img: Optional[str] = None
    created_at: datetime
