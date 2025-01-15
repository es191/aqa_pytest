import requests
from utils.custom_functions import CustomFunctions as cf

def test_yahoo_finance_quotes(api_config):
    """Checking the Yahoo Finance API to get quotes."""
    response = requests.get(
        url=f"{api_config['API_URL']}/market/v2/get-quotes",
        headers=api_config["HEADERS"],
        params= {
            'region': api_config['PARAMS']['region'],
            'symbols': api_config['PARAMS']['symbols'],
        },
    )
    assert response.status_code == 200

    data = response.json()
    quote_response = data["quoteResponse"]

    assert "quoteResponse" in data
    assert "error" in quote_response
    assert quote_response["error"] is None
    assert "result" in quote_response
    assert isinstance(quote_response["result"], list)
    assert len(quote_response["result"]) > 0


def test_yahoo_finance_earnings(api_config):
    """Checking the Yahoo Finance API to get earnings."""
    
    response = requests.get(
        url = f"{api_config['API_URL']}/market/get-earnings",
        headers=api_config["HEADERS"],
        params = {
            'region': api_config['PARAMS']['region'],
            'startDate': cf.get_current_timestamp_millis(6),
            'endDate': cf.get_current_timestamp_millis(),
            'size': cf.get_random_number(),
    }
    )
    
    print(response.url)
    assert response.status_code == 200

    data = response.json()
    finance = data["finance"]

    assert "finance" in data
    assert "error" in finance
    assert finance["error"] is None
    assert "result" in finance
    assert isinstance(finance["result"], list)
    assert len(finance["result"]) > 0
    
