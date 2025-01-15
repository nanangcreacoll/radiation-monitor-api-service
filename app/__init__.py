from fastapi import FastAPI
import os
from dotenv import load_dotenv
from prisma import Prisma
from contextlib import asynccontextmanager

from config.app import App
from config.log import Log
from routers import root_router

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

app.include_router(
    router=root_router,
    tags=["root"],
    include_in_schema=False
)
