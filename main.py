from urllib.parse import urlparse

import requests

TOKEN = 'bea9269e049610978b0d58bc7138ad57fb3ab5de'
API_SHORTEN_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
API_URL_COUNTER = 'https://api-ssl.bitly.com/v4//bitlinks/{}/clicks/summary'


def shorten_url(token, url):
    json = {"long_url": url}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(API_SHORTEN_URL, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, user_input):
    parsed_url = urlparse(user_input)
    url_without_scheme = parsed_url.netloc + parsed_url.path
    print(url_without_scheme)
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        "unit": "day",
        "unites": -1
    }
    response = requests.get(
        API_URL_COUNTER.format(url_without_scheme),
        params=params,
        headers=headers
    )
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    user_url = input("Please enter url: ")
    try:
        url = shorten_url(TOKEN, user_url)
        print('Битлинк', url)
    except requests.exceptions.HTTPError:
        print("You have entered incorrect url")

    try:
        print(count_clicks(TOKEN, url))
    except requests.exceptions.HTTPError:
        print("You have entered incorrect URL")
