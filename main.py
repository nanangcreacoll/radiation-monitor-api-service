from dotenv import load_dotenv
import os
import asyncio

load_dotenv(override=True)

if __name__ == "__main__":
    from config.app import App
    from config.log import Log

    logger = Log().get_logger(__name__)
    config = App()

    if os.getenv("NODE_ENV") == "development":
        logger.info("Running application in development")
        config.run()
    elif os.getenv("NODE_ENV") == "production":
        logger.info("Running application in production")
        asyncio.run(config.serve())
