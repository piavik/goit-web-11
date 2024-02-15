from datetime import date
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50,  description="First name")
    last_name:  str = Field(max_length=50,  description="Last name")
    email:      str = Field(max_length=100, description="email")  
    phone:      str = Field(max_length=15,  description="Phone number")
    birthday:   date
    notes:      str



class ContactResponse(ContactModel):
    id:         int
    first_name: str
    last_name:  str
    email:      str
    phone:      str
    birthday:   date 
    notes:      str

    class Config:
        from_attributes = True
