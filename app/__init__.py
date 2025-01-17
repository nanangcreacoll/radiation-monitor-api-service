from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from config.app import App
from config.log import Log
from config.prisma import prisma
from routers import root_router
from routers import user_router

load_dotenv(override=True)

logger = Log().get_logger(__name__)

config = App()


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
    lifespan=lifespan,
)

app.include_router(router=root_router, tags=["root"], include_in_schema=False)

app.include_router(router=user_router, prefix=config.prefix, tags=["user"])
