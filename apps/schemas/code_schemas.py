from pydantic import BaseModel, Field, ConfigDict, EmailStr

class CodeGenerateSchema(BaseModel):
    email: EmailStr = Field(min_length=4, max_length=50)
    id_user: int | None = Field(None, gt=0)

class CodeValidateSchema(BaseModel):
    email: EmailStr = Field(min_length=4, max_length=50)
    user_code: int = Field(gt=999, lt=10000)
    id_user: int | None = Field(None, gt=0)
    
class CodeResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    message: str
    valid: bool