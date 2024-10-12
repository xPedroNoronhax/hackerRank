import sys
import requests
import json


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()


usd_rate = data['bpi']['USD']['rate'].replace(',', '')


usd_rate = float(usd_rate)


if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:

    multiple = float(sys.argv[1])
except ValueError:

    print("Command-line argument is not a number")
    sys.exit(1)


result = usd_rate * multiple
print(f"${result:,.4f}")
