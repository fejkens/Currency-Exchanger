import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

dotenv_path = join(dirname(__file__), '.gitignore/.env')
load_dotenv(dotenv_path)

BASE_URL = 'https://www.amdoren.com/api/currency.php'
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

req = requests.get(f'{BASE_URL}?api_key={CURRENCY_API_KEY}&from=USD&to=GBP&amount=1')
print(req)


