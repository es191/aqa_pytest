import requests
from utils.custom_functions import CustomFunctions as cf

def test_yahoo_news_get_news(api_config):
    """Checking the Yahoo Finance API to get the list of news."""
    response = requests.post(
        url=f"{api_config['API_URL']}/news/v2/list",
        headers={
            "x-rapidapi-host": api_config["HEADERS"]["x-rapidapi-host"],
            "x-rapidapi-key": api_config["HEADERS"]["x-rapidapi-key"],
            "Content-Type": api_config["HEADERS"]["Content-Type"],
        },
        params= {
            'region': api_config['PARAMS']['region'],
            'snippetCount': api_config['PARAMS']['snippetCount'],
        },
        data= api_config["DATA"]["pagination"]
    )
    data = response.json()

    assert response.status_code == 200
    assert api_config["DATA"]["pagination"]["uuids"] in data["data"]["ntk"]["pagination"]["uuids"]
    assert data["data"]["main"]["nextPage"] is True
    

