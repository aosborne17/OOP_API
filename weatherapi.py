import requests
import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 22)

city_names = ["London", "Paris", "Barcelona", "Prague", "Madrid", "Edinburgh", "Melbourne", "Tokyo", "Taiwan"]
api_key = "b5a227e7202c471b6e3efac5f6880837"

# this gets the dat and puts it into json form

df_all_current_weather = pd.DataFrame()

# Create empty lists to store the JSON Data

prediction_num = 0
current_weather_id = []
current_time = []
own_city_id = []
city = []
latitude = []
longitude = []
country = []
timezone = []
sunrise = []
sunset = []
temperature = []
temperature_feel = []
temperature_min = []
temperature_max = []
pressure = []
humidity = []
main = []
main_description = []
clouds = []
wind_speed = []
wind_degree = []
visibility = []

# Add JSON Data to the lists


for elements in city_names:

    url1 = f'http://api.openweathermap.org/data/2.5/weather?q={elements}&appid={api_key}'
    city_data = requests.get(url1).json()

    prediction_num +=1
    current_weather_id.append(prediction_num + 1)
    current_time.append(pd.Timestamp.now())
    own_city_id.append(city_data['id'])
    city.append(city_data['name'])
    latitude.append(city_data['coord']['lat'])
    longitude.append(city_data['coord']['lon'])
    country.append(city_data['sys']['country'])
    if city_data['timezone'] >0 :
        timezone.append(("+" + str((city_data['timezone']) / 3600)))
    else:
        timezone.append(((city_data['timezone']) / 3600))
    sunrise.append(city_data['sys']['sunrise'])
    sunset.append(city_data['sys']['sunset'])
    temperature.append(city_data['main']['temp'])
    temperature_feel.append(city_data['main']['feels_like'])
    temperature_min.append(city_data['main']['temp_min'])
    temperature_max.append(city_data['main']['temp_max'])
    pressure.append(city_data['main']['pressure'])
    humidity.append(city_data['main']['humidity'])
    main.append(city_data['weather'][0]['main'])
    main_description.append(city_data['weather'][0]['description'])
    clouds.append(city_data['clouds']['all'])
    wind_speed.append(city_data['wind']['speed'])
    wind_degree.append(city_data['wind']['deg'])
    visibility.append(city_data['visibility'])



# Write Lists to DataFrame

df_all_current_weather['current_weather_id'] = current_weather_id
df_all_current_weather['current_time'] = current_time
df_all_current_weather['own_city_id'] = own_city_id
df_all_current_weather['city'] = city
df_all_current_weather['latitude'] = latitude
df_all_current_weather['longitude'] = longitude
df_all_current_weather['country'] = country
df_all_current_weather['timezone'] = timezone
df_all_current_weather['sunrise'] = sunrise
df_all_current_weather['sunset'] = sunset
df_all_current_weather['temperature'] = temperature
df_all_current_weather['temperature_feel'] = temperature_feel
df_all_current_weather['temperature_min'] = temperature_min
df_all_current_weather['temperature_max'] = temperature_max
df_all_current_weather['pressure'] = pressure
df_all_current_weather['humidity'] = humidity
df_all_current_weather['main'] = main
df_all_current_weather['main_description'] = main_description
df_all_current_weather['clouds'] = clouds
df_all_current_weather['wind_speed'] = wind_speed
df_all_current_weather['wind_degree'] = wind_degree
df_all_current_weather['visibility'] = visibility

print(df_all_current_weather.head(10))