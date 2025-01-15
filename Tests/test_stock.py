import requests
from utils.custom_functions import CustomFunctions as cf

def test_yahoo_stock_get_summary(api_config):
    """Checking the Yahoo Finance API to get stock summary."""
    response = requests.get(
        url=f"{api_config['API_URL']}/stock/v2/get-summary",
        headers=api_config["HEADERS"],
        params= {
            'symbol': api_config['PARAMS']['symbol'],
            'region': api_config['PARAMS']['region'],
        },
    )
    assert response.status_code == 200

    data = response.json()

    assert "defaultKeyStatistics" in data
    assert "summaryProfile" in data
    assert data ["summaryProfile"]["longBusinessSummary"] is not None
    assert "price" in data
    assert data["symbol"] == api_config['PARAMS']['symbol']


def test_yahoo_stock_events_calendar(api_config):
    """Checking the Yahoo Finance API to get events calendar."""
    response = requests.get(
        url=f"{api_config['API_URL']}/stock/get-events-calendar",
        headers=api_config["HEADERS"],
        params= {
            'tickersFilter': api_config['PARAMS']['tickersFilter'],
            'modules': api_config['PARAMS']['modules'],
        },
    )
    assert response.status_code == 200

    data = response.json()

    assert "finance" in data
    assert "result" in data["finance"]
    assert "error" in data["finance"]