import requests
from datetime import datetime, date, time


def weather(openweather_token):
    dt = datetime.now()
    dt = dt.date()
    s_city = "Moscow, RU"
    city_id = 0
    appid = openweather_token
    msgshrt = f'Погода в Москве {dt}:\n'
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        #print("city:", cities)
        city_id = data['list'][0]['id']
        #print('city_id=', city_id)
    except Exception as e:
        print("Exception (find):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                     params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()


        condition=data['weather'][0]['description']
        # print("temp:", data['main']['temp'])
        # print("temp_min:", data['main']['temp_min'])
        temp=int(data['main']['temp'])


        # print("temp_max:", data['main']['temp_max'])
        pressure=data['main']['pressure']
        humidity=data['main']['humidity']
        msgshrt+=f'''{condition}
Температура:{temp}*С
Давление: {pressure} ММРТС 
Влажность воздуха: {humidity}%\n
'''
    except Exception as e:
        print("Exception (weather):", e)
        pass
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        # print(data)

        # for i in data['list']:
        #      print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
    except Exception as e:
        print("Exception (forecast):", e)
        pass
    msglong = ''
    return msgshrt, msglong
