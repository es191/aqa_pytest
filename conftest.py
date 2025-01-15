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
            "size": 12,
            "symbol": "AMRN",
            "symbols": "AMD,IBM,AAPL",
            "tickersFilter": "AMRN",
            "modules": "ipoEvents,earnings,secReports"
        },
    }
