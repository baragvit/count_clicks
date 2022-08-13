import requests

url = 'https://api-ssl.bitly.com/v4/user'

headers = {
    'Authorization': 'Bearer bea9269e049610978b0d58bc7138ad57fb3ab5de'
}
response = requests.get(url, headers=headers)
print(response.text)