import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import sys

# Load the environment variables from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Grab the environment variables
BASE_URL = os.getenv('BASE_URL')
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')


def main():

    # Grab the sys arguments passed in when program is started
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print('The first argument has to be a valid number')
        sys.exit()
    except IndexError:
        print('Incorrect number of arguments. Usage: py .\exchange.py amount base_currency_code to_currency_code')
        sys.exit()

    try:
        base = sys.argv[2]
        to = sys.argv[3]
    except IndexError:
        print('Incorrect number of arguments. Usage: py .\exchange.py amount base_currency_code to_currency_code')
        sys.exit()

    exchange_rate = fetch_exchange_rate(amount, base, to)

    # Calculate the resulting amount of the exchange
    exchange_result = amount * exchange_rate

    # Print out the result of the exchange
    message = f'{amount} {base} = {round(exchange_result, 2)} {to} ({round(exchange_rate, 5)} EX)'
    print(message)


def fetch_exchange_rate(amount, base, to):

    symbols = base + ',' + to

    # Make the API call and get the json result
    req = requests.get(f'{BASE_URL}?access_key={CURRENCY_API_KEY}&symbols={symbols}&amount={amount}')
    req = req.json()

    # Since we can't change the base currency on this API, we have to calculate the exchange rate ourselves
    try: 
        exchange_rate = req["rates"][to] / req["rates"][base]
    except KeyError:
        print('Invalid currencies. Please use the correct three-letter currency codes.')
        sys.exit()

    return exchange_rate


if __name__ == '__main__':
    main()

