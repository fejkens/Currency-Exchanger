import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import sys

dotenv_path = join(dirname(__file__), '.gitignore/.env')
load_dotenv(dotenv_path)

BASE_URL = 'https://www.amdoren.com/api/currency.php'
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

def main():

    amount = sys.argv[1]
    base = sys.argv[2]
    to = sys.argv[3]

    req = requests.get(f'{BASE_URL}?api_key={CURRENCY_API_KEY}&from={base}&to={to}&amount={amount}')

if __name__ == '__main__':
    main()