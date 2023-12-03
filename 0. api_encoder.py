import requests
import pandas as pd
api_key = 'Z6C1HNUPI5WSAHMPD4EM3V54FQDQ7PC6GQ'

''' function to fetch raw ether data from etherscan API '''

def get_raw_data(address, apikey=api_key):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": "0", 
        "endblock": "99999999", 
        "apikey": apikey
    }

    response = requests.get(url, params=params, timeout=60)
    if response.status_code == 200:
        data = response.json()
        res = data['result']
        return res
    else:
        print(f"Error: {response.status_code} - {response.text}")