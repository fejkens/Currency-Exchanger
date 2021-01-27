import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import sys

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BASE_URL = os.getenv('BASE_URL')
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

def main():

    amount = int(sys.argv[1])
    base = sys.argv[2]
    to = sys.argv[3]
    symbols = base + ',' + to

    req = requests.get(f'{BASE_URL}?access_key={CURRENCY_API_KEY}&symbols={symbols}&amount={amount}')
    req = req.json()

    exchange_rate = req["rates"][to] / req["rates"][base]

    exchange_result = format(amount * exchange_rate, '.2f')

    exchange_rate = format(exchange_rate, '.5f')

    message = f'{amount} {base} = {exchange_result} {to} ({exchange_rate} EX)'
    print(message)

if __name__ == '__main__':
    main()

