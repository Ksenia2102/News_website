from flask import current_app
import requests

def weather_by_city(city_name):
    wearther_url = current_app.config['WEATHER_URL']
    params = {
        'key': current_app.config['WEATHER_APP_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': 1, 
        'lang': 'ru'
    }
    try:
        result = requests.get(wearther_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        'Сетевая ошибка'
        return False  
    return False


if __name__ == '__main__':
    w = weather_by_city('Moscow,Russia')
    print(w)