import requests

# https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/


def get_weather():

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "675dc6ba1e1b587134b1b61ddb1b0c20"
    CITY = "Chichester"

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # catches HTTP errors (404, 401, etc.)
        data = response.json()
        weather = data["weather"][0]["main"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        result = ["Weather:",
                  weather,
                  "Temperature:",
                  round(temp_celsius, 1),
                  "°C"]
        return result
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except requests.exceptions.ReadTimeout as errrt:
        print("Time out")
    except requests.exceptions.ConnectionError as conerr:
        print("Connection error")
    except requests.exceptions.RequestException as errex:
        print("Exception request")
