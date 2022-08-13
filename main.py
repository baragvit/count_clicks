import requests

me_url = 'https://api-ssl.bitly.com/v4/user'

headers = {
    'Authorization': 'Bearer bea9269e049610978b0d58bc7138ad57fb3ab5de'
}
response = requests.get(me_url, headers=headers)
print(response.text)



data = {
    "long_url": "http://dvmn.org"
}

shorten_url = 'https://api-ssl.bitly.com/v4/bitlinks'
response = requests.post(shorten_url, headers=headers, json=data)
print(response.json())