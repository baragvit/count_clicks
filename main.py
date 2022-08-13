from urllib.parse import urlparse

import requests

TOKEN = 'bea9269e049610978b0d58bc7138ad57fb3ab5de'
API_SHORTEN_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
API_URL_COUNTER = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
API_BITLINK_INFO = 'https://api-ssl.bitly.com/v4/bitlinks/{}'


def shorten_url(token, url):
    json = {"long_url": url}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(API_SHORTEN_URL, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, user_input):
    parsed_url = urlparse(user_input)
    url_without_scheme = parsed_url.netloc + parsed_url.path
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


def is_bitlink(token, user_url):
    parsed_url = urlparse(user_url)
    url_without_scheme = parsed_url.netloc + parsed_url.path
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(
        API_BITLINK_INFO.format(url_without_scheme),
        headers=headers
    )
    return response.ok


if __name__ == '__main__':
    user_url = input("Please enter url: ")
    is_link = is_bitlink(TOKEN, user_url)
    func = count_clicks if is_link else shorten_url
    try:
        result = func(TOKEN, user_url)
        print(result if is_link else 'Битлинк: ' + result)
    except requests.exceptions.HTTPError as err:
        print("You have entered incorrect url")
