import os
import pytest
from dotenv import load_dotenv 
from utils.custom_functions import CustomFunctions as cf

load_dotenv()

@pytest.fixture(scope="session")
def api_config():
    return {
        "API_URL": os.getenv("API_URL"),
        "HEADERS": {
            "x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
            "Content-Type": "text/plain",
        },
        "PARAMS": {
            "region": "US",
            "tickersFilter": "AMRN",
            "modules": "ipoEvents,earnings,secReports",
            "symbols": "AMD,IBM,AAPL",
            "symbol": "AMRN",
            "size": cf.get_random_number(),
            "snippetCount": cf.get_random_number()
        },
        "DATA": {
            "pagination": {"requestedCount":0,"remainingCount":0,"uuids":""}
        }
    }
