import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.gitignore/.env')
load_dotenv(dotenv_path)

key = os.getenv('CURRENCY_API_KEY')

print(key)