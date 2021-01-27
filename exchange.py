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

    amount = sys.argv[1]
    base = sys.argv[2]
    to = sys.argv[3]
    symbols = base + ',' + to

    req = requests.get(f'{BASE_URL}?access_key={CURRENCY_API_KEY}&symbols={symbols}&amount={amount}')
    print(req.json())

if __name__ == '__main__':
    main()

