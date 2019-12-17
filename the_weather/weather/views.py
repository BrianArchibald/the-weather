import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=32ebc86efd4714fb9ea0f0aa950118d0'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()
    print(r.text)

    city_weather = {
            'city': city,
            'temperate': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            }

    context = {'city_weather': city_weather}

    return render(request, 'weather/weather.html', context)
