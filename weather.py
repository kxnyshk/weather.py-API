# imports
import sys
import time
import requests
from urllib import response

# API setup
API_KEY = "4643783a875af031bbfc48ab5ccd541b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather/"

# globals
ERR = '\nOops! bad gateway, an error occured.'
INV = '\nInvalid command!'

# methods
def display(city, data):
    city = city.capitalize()
    
    lon = data['coord']['lon']
    lat = data['coord']['lat']
    loc = f"\nYour location is ({lon}, {lat})"

    des = data['weather'][0]['description']
    tem = round(data['main']['temp'] - 273.15, 2)
    max = round(data['main']['temp_max'] - 273.15, 2)
    min = round(data['main']['temp_min'] - 273.15, 2)
    wea = f"\nIt's {tem}°C today in {city} with {des}.\nMax temp will be around {max} and min around {min}"

    pre = round(data['main']['pressure'] / 1013.25, 2)
    hum = data['main']['humidity']
    vis = data['visibility'] / 1000
    win = data['wind']['speed']
    atm = f"\nThe pressure today is {pre} Atm. Humidity at {hum}%.\nVisibility at {vis} meters. Wind speed at {win} m/s."

    ris = data['sys']['sunrise']
    set = data['sys']['sunset']
    tim = f'\nSunrise at {time.strftime("%H:%M", time.localtime(ris))} AM\nSunset at {time.strftime("%H:%M", time.localtime(set))} PM'
    
    def key():
        key_ = input('\n> ')
        
        match key_:
            case '1':
                print(loc)
            case '2':
                print(wea)
            case '3':
                print(atm)
            case '4':
                print(tim)
            case '0':
                sys.exit()
            case _:
                print(INV)
        
        key()

    key()

def help(city, data):
    press = '\nPress:'
    loc = '1 for location'    # co-ord
    wea = '2 for weather'     # desc / temp / max / min
    atm = '3 for atmospheric details' # pressure / humidity / visibility / wind
    tim = '4 for timings'     # sunrise / sunset / timezone
    end = '0 to exit'         # exit

    print(press)
    print(loc)
    print(wea)
    print(atm)
    print(tim)
    print(end)

    display(city, data)

# main exe
def main():
    city = input("\nEnter your city: ")
    req_url = f'{BASE_URL}?q={city}&appid={API_KEY}'

    fetch = requests.get(req_url)

    if (fetch.status_code == 200):
        data = fetch.json()
        # print(data)
        help(city, data)
    else:
        print(ERR)

# test
main()
