from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str

    @field_validator("password")
    @classmethod
    def password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Пароль має бути не менше 8 символів")
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль повинен містити хоча б одну цифру")
        if not any(c.isalpha() for c in v):
            raise ValueError("Пароль повинен містити хоча б одну літеру")
        return v

class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str

class Token(BaseModel):

    token_type: str
    access_token: str

    class Config:
        from_attributes = True