from pydantic import BaseModel, ConfigDict
from typing import List, Optional

# User Table Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    posts: List["PostResponse"] = []

    model_config = ConfigDict(from_attributes=True)

# Post Table Schemas
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)