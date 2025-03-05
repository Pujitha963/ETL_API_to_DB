import requests

#using openweather api key
API_KEY = '7163eb86dc5fb90914c4ba1cb5b77eb2'
CITY = 'Hyderabad'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data')
        return None
