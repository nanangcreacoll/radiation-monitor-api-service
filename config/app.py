from .log import Log
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)
logger = Log().get_logger(__name__)

class App:
    def __init__(self):
        self.host = os.getenv("APP_HOST", "localhost")
        self.port = int(os.getenv("APP_PORT", 8000))
        self.prefix = os.getenv("APP_PREFIX", "/api")
        self.title = os.getenv("APP_TITLE", "FastAPI")
        self.version = os.getenv("APP_VERSION", "0.1.0")
        self.docs_url = os.getenv("APP_DOCS_URL", "/api/docs")
        self.redoc_url = os.getenv("APP_REDOC_URL", "/api/redoc")
        self.openapi_url = os.getenv("APP_OPENAPI_URL", "/api/openapi.json")

        self.__log_level = os.getenv("APP_LOG_LEVEL", "INFO")
        self.__reload = os.getenv("APP_RELOAD", False)

    def run(self):
        import uvicorn
        
        logger.info(f"Running {self.title} v{self.version} on {self.host}:{self.port}")

        uvicorn.run(
            app="app:app",
            host=self.host,
            port=self.port,
            reload=self.__reload,
            reload_delay=1,
            log_level=self.__log_level.lower()
        )

    async def serve(self):
        import uvicorn

        logger.info(f"Serving {self.title} v{self.version} on {self.host}:{self.port}")

        config = uvicorn.Config(
            app="app:app",
            host=self.host,
            port=self.port,
            log_level=self.__log_level.lower()
        )
