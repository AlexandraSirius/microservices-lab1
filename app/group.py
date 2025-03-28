from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Group(BaseModel):
    ID: int
    Title: str
    Description: str
    Contacts: List[int]

@router.post("/")
def create_group(group: Group):
    return group

@router.get("/")
def read_group():
    return Group(ID=1, Title="Test Group", Description="Just testing", Contacts=[1, 2, 3])

@router.put("/")
def update_group(group: Group):
    return group

@router.delete("/")
def delete_group():
    return {"status": "deleted"}
