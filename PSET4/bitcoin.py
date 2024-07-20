# This is a simple application which will help users, who want to buy Bitcoin, know right away the price of Bitcoin in USD.
# This application uses API request.
# This will accept a float command-line argument, which is the number of Bitcoin

# import required libraries: sys and requests
import sys
import requests

# ensure that user provides a command-line argument that would represent the number of Bitcoin.
# so, the length of the command-line arguments should be two, and the second argument is the number of coin.
# if the user doesn't cooperate the requirement, exit the program, providing the error.
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    numCoin = float(sys.argv[1])
except (TypeError, ValueError) as e:
    sys.exit("Command-line argument is not a number")

# use requests library to retrieve the Bitcoin data using its API.
# catch RequestException, an ambiguous error, which can happen when handling the request.
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    formatR = r.json()
except request.RequestException:
    sys.exit("An error in requesting the API call")

# retrieve the Bitcoin price
bitcoinPrice = formatR["bpi"]["USD"]["rate_float"]

# the price for the number of coins that user wants to buy
amount = numCoin * bitcoinPrice

# format the output with comma separated value and four decimal place.
print(f"${amount:,.4f}")
