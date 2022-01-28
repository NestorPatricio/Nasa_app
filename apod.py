import requests
import json
from random import choices
from data import API_KEY
from get_module import get_nasa

def pull_photos(n, total = 50, api = API_KEY):
    url = f'https://api.nasa.gov/planetary/apod?count={total}&api_key={api}'
    resultado = get_nasa(url)
    pool_fotos = [elemento for elemento in resultado if elemento['media_type'] == 'image']
    return choices(pool_fotos, k = n)

if __name__ == '__main__':
    print(pull_photos(2))