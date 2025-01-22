# Check APP_SECRET_KEY in .env file

import os

from dotenv import load_dotenv

load_dotenv(override=True)


async def check_app_secret_key():
    env_file = ".env"
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parent_dir = os.path.dirname(script_dir)
    env_file = os.path.join(parent_dir, env_file)
    secret_key = os.getenv("APP_SECRET_KEY")
    # Check if .env file exists
    # If not, raise FileNotFoundError
    # If exists, check if APP_SECRET_KEY exists
    # If not, raise KeyError

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"{env_file} does not exist.")

    if not secret_key:
        raise KeyError(
            f"APP_SECRET_KEY does not exist in {env_file}, please set it or generate it with tools/generate_key.py"
        )
