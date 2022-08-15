# Bitly URL shortener
Shorten provided urls and provide there count  
Usage
```
python3 main.py
```

### How to install
Python3 should already be installed.   
Create and activate virtual environment
```commandline
python3 -m venv venv
source venv/bin/activate
```
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Get api bitly api token, place it to .env file in count_clicks directory
```commandline
cd count_clicks
echo "API_TOKEN=bea0000e049610978b0d58bc7138ad57fb3ab5de" >> .env
```
### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).