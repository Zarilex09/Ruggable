import requests



# Define the API endpoint URL
url = "https://api.etherscan.io/api"

# Define the parameters for the API request
params = {
    "module": "account",
    "action": "txlist",
    "address": "0x062082fe1e7c5dfa7729fbf0d330b9bf65cde510", #reolace this
    "startblock": "0", 
    "endblock": "99999999", 
    "apikey": "KCMY95HPGBY5CKC9PYY8FSVVAB89U5EZKU",  # Replace with your actual API key token
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract the balance from the response
    res = data['result']
    print(res)

else:
    print(f"Error: {response.status_code} - {response.text}")