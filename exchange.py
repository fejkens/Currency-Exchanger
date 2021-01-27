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
    amount = int(sys.argv[1])
    base = sys.argv[2]
    to = sys.argv[3]
    symbols = base + ',' + to

    # Make the API call and get the json result
    req = requests.get(f'{BASE_URL}?access_key={CURRENCY_API_KEY}&symbols={symbols}&amount={amount}')
    req = req.json()

    # Since we can't change the base currency on this API, we have to calculate it ourselves
    exchange_rate = req["rates"][to] / req["rates"][base]

    # Calculate the resulting amount of the exchange
    exchange_result = format(amount * exchange_rate, '.2f')

    # Format the exchange rate to 5 decimal places
    exchange_rate = format(exchange_rate, '.5f')

    # Print out the result of the exchange
    message = f'{amount} {base} = {exchange_result} {to} ({exchange_rate} EX)'
    print(message)

if __name__ == '__main__':
    main()

