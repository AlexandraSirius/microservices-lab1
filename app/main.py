from fastapi import FastAPI
from app import contact, group

app = FastAPI()

app.include_router(contact.router, prefix="/api/v1/contact")
app.include_router(group.router, prefix="/api/v1/group")
