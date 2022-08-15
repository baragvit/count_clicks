import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

API_SHORTEN_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
API_URL_COUNTER = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
API_BITLINK_INFO = 'https://api-ssl.bitly.com/v4/bitlinks/{}'


def shorten_url(token, url):
    response = requests.post(
        API_SHORTEN_URL,
        headers=get_auth_header(token),
        json={"long_url": url}
    )
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, user_input):
    parsed_url = urlparse(user_input)
    response = requests.get(
        API_URL_COUNTER.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers=get_auth_header(token)
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, user_url):
    parsed_url = urlparse(user_url)
    response = requests.get(
        API_BITLINK_INFO.format(f'{parsed_url.netloc}{parsed_url.path}'),
        headers=get_auth_header(token)
    )
    return response.ok


def get_auth_header(token):
    return {'Authorization': f'Bearer {token}'}


if __name__ == '__main__':
    load_dotenv()
    api_token = os.environ['API_TOKEN']
    user_url = input("Please enter url: ")
    try:
        if is_bitlink(api_token, user_url):
            clicks_count = count_clicks(api_token, user_url)
            print(clicks_count)
        else:
            bitly_url = shorten_url(api_token, user_url)
            print(f'Битлинк: {bitly_url}')
    except requests.exceptions.HTTPError as err:
        print("You have entered incorrect url")
