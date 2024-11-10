import sys
import requests

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Missing command-line argument")
    else:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        info = bitcoin.json()
        price = info["bpi"]["USD"]["rate_float"]
        amount = float(price)*float(sys.argv[1])
        print(f"${amount:,.4f}")
except requests.RequestException:
    pass