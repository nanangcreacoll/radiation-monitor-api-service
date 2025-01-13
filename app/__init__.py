from fastapi import FastAPI
from config.app import App
from config.log import Log
import os
from dotenv import load_dotenv
from prisma import Prisma
from contextlib import asynccontextmanager

load_dotenv(override=True)

logger = Log().get_logger(__name__)

config = App()

prisma = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    try:
        yield
    finally:
        await prisma.disconnect()


app = FastAPI(
    title=config.title,
    version=config.version,
    docs_url=config.docs_url,
    redoc_url=config.redoc_url,
    openapi_url=config.openapi_url,
    lifespan=lifespan
)

@app.get("/")
async def read_root():
    return {"data": "Hello World"}
