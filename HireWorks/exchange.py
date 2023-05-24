import requests
import json

APIKey="UIOMgciPB5rYw6QzaHrwo1aMGPoIFON8"

def exchange_amount(target_currency,amount):
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={target_currency}&from=USD&amount={amount}"
    payload = {}
    headers= {
       "apikey":APIKey
    }
    print(url)
    response = requests.request("GET", url, headers=headers, data = payload)
    if response.status_code == 200:
        data = response.json()
        result = data['result']
        return result 
    else:
        print(response)
        return None