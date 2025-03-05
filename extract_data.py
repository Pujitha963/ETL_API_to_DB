import requests

#using openweather api key
API_KEY = 'api_kpi' #replace with actual one
CITY = 'Hyderabad'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def extract():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch data')
        return None
