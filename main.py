from dotenv import load_dotenv
import os
import requests

load_dotenv()

JUMPSELLER_LOGIN = os.getenv('JUMPSELLER_LOGIN')
JUMPSELLER_AUTH_TOKEN = os.getenv('JUMPSELLER_AUTH_TOKEN')

STORE = 'ferreteriamfs'  

BASE_URL = 'https://api.jumpseller.com/v1'
ENDPOINT = '/products.json'
url = BASE_URL + ENDPOINT
response = requests.get(url, auth=(JUMPSELLER_LOGIN, JUMPSELLER_AUTH_TOKEN))

print(response.status_code)
print(response.json())