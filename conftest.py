import os
import pytest
from dotenv import load_dotenv 

load_dotenv()

@pytest.fixture(scope="session")
def api_config():
    return {
        "API_URL": os.getenv("API_URL"),
        "HEADERS": {
            "x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        },
        "PARAMS": {
            "region": "US",
            "symbols": "AMD,IBM,AAPL",
            "size": 12,
        },
    }
