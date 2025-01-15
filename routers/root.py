from fastapi import APIRouter
from config.app import App

router = APIRouter()
config = App()

welcome_message = f"Welcome to {config.title}"

@router.get("/")
async def welcome():
    return {"message": welcome_message}

@router.get("/api")
async def welcome_api():
    return {"message": f"{welcome_message}"}
