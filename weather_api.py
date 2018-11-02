import requests
from pprint import pprint


city = input("enter the city name:")
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=87a0a68214c49b56360f51321429cbde&units=metric".format(city)
res = requests.get(url)
data = res.json()
#pprint(res)
#pprint(data)


temp = data["main"]["temp"]
humid = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]

latitude = data["coord"]["lat"]
longitude = data["coord"]["lon"]
weather = data["weather"][0]["description"]



print("tenperature : {} degree celcius".format(temp))
print("humidity :{}".format(humid))
print("wind_speed : {} m/s".format(wind_speed))

print("latitude : {}".format(latitude))
print("longitude : {}".format(longitude))
print("desription :{}".format(weather))

