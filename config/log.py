import logging
import os
import sys
from dotenv import load_dotenv

load_dotenv(override=True)

class Log:
    def __init__(self):
        self.__log_level = os.getenv("APP_LOG_LEVEL", "INFO")
        self.__log_format = os.getenv("APP_LOG_FORMAT", "%(asctime)s\t%(levelname)s\t[%(name)s]\t%(message)s")
        self.__log_file = os.getenv("APP_LOG_FILE", "app.log")
        self.__log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.getenv("APP_LOG_DIR", "logs"))
        self.__log_path = f"{self.__log_dir}/{self.__log_file}"

        os.makedirs(self.__log_dir, exist_ok=True)

        self.__setup_logging()
        self.__suppress_httpx_logs()

    def __get_log_level(self):
        level = self.__log_level.upper()
        levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        return levels.get(level, logging.INFO)

    def __setup_logging(self):
        file_handler = logging.FileHandler(self.__log_path)
        file_handler.setFormatter(logging.Formatter(self.__log_format))

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.addFilter(lambda record: record.levelno < logging.ERROR)
        stdout_handler.setFormatter(logging.Formatter(self.__log_format))

        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.ERROR) 
        stderr_handler.setFormatter(logging.Formatter(self.__log_format))

        logging.basicConfig(
            level=self.__get_log_level(),
            handlers=[file_handler, stdout_handler, stderr_handler]
        )

    def __suppress_httpx_logs(self):
        httpx_logger = logging.getLogger("httpx")
        httpx_logger.setLevel(logging.WARNING)
        httpx_logger.propagate = False

    def get_logger(self, name):
        return logging.getLogger(name)
