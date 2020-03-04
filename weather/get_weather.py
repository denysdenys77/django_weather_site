import requests
import datetime
from datetime import datetime


class APIError(Exception):
    pass


class Weather:

    base_url = 'http://api.openweathermap.org'
    app_id = '4b0474b68bb0012daed655d182e69e2a'

    def send_request(self, url):
        res = requests.get(url)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            raise APIError()
        return res.json()

    def get_current_weather(self, user_cities_list):

        url_type = 'current_weather'

        context = {
            'city_list': []
        }

        for city in user_cities_list:
            url = self.create_url(city, url_type)
            weather = self.send_request(url)

            city_dict = {
                'name': city.city,
                'temp': weather['main']['temp'],
                'wind': weather['wind']['speed'],
                'description': weather['weather'][0]['description'],
            }

            context['city_list'].append(city_dict)

        return context

    def get_five_days_weather(self, city):

        url_type = 'five_days_weather'

        url = self.create_url(city, url_type)

        weather = self.send_request(url)

        # get today's date
        now = datetime.now()
        dt_string = now.strftime("%d")
        date_to_view = str(now)[:10]

        five_days_list = weather['list']

        # air temperature for today
        current_weather = weather['list'][0]['main']['temp']
        current_wind = weather['list'][0]['wind']['speed']
        current_description = weather['list'][0]['weather'][0]['description']

        weather_ready = []

        for day in five_days_list[1:]:

            date = day['dt_txt'][8:10]
            time = day['dt_txt'][11:13]

            if time == '12' and date != dt_string:
                day['dt_txt'] = day['dt_txt'][:10]
                weather_ready.append(day)

        context = {
            'city': city,
            'today_day': date_to_view,
            'today_temp': current_weather,
            'current_wind': current_wind,
            'current_description': current_description,
            'weather_ready': weather_ready,
        }

        return context

    def create_url(self, city, url_type):
        if url_type is 'current_weather':
            url = f'{self.base_url}/data/2.5/weather?q={city}&appid={self.app_id}&units=metric'
            return url
        elif url_type is 'five_days_weather':
            url = f'{self.base_url}/data/2.5/forecast?q={city}&appid={self.app_id}&units=metric'
            return url


