import requests

TOKEN = 'bea9269e049610978b0d58bc7138ad57fb3ab5de'
API_SHORTEN_URL = 'https://api-ssl.bitly.com/v4/bitlinks'


def shorten_url(token, url):
    json = {"long_url": url}
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(API_SHORTEN_URL, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['link']


if __name__ == '__main__':
    dvmn_url = "https://dmvn.org"
    print('Битлинк', shorten_url(TOKEN, dvmn_url))
