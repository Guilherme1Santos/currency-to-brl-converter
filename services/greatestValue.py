import requests
#will return the current value, and the highest value reached in the last 24 hours
def searchCurrency(currency):
    URL = f'https://economia.awesomeapi.com.br/last/{currency}-BRL'
    req = requests.get(URL)
    if req.status_code == 200:
        data = req.json()[f"{currency}BRL"]
        return {
             "atual": data["bid"],
             "max_24h": data["high"],
             "min_24h": data["low"]
         }
    else:
        return "Moeda não encontrada!"