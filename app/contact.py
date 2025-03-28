from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Phone(BaseModel):
    TypeID: int
    CountryCode: int
    Operator: int
    Number: int

class Contact(BaseModel):
    ID: int
    Username: str
    GivenName: str
    FamilyName: str
    Phone: List[Phone]
    Email: List[str]
    Birthdate: str

@router.post("/")
def create_contact(contact: Contact):
    return contact

@router.get("/")
def read_contact():
    return Contact(
        ID=1,
        Username="testuser",
        GivenName="Test",
        FamilyName="User",
        Phone=[],
        Email=[],
        Birthdate="1990-01-01"
    )

@router.put("/")
def update_contact(contact: Contact):
    return contact

@router.delete("/")
def delete_contact():
    return {"status": "deleted"}
