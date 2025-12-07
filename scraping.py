import requests
from bs4 import BeautifulSoup

path_to_scrape = requests.get("https://weather.com/en-GB/weather/today/l/152a40546e6d49414c4d9d16186455f7414bfa1dca14f6d8649366035a1af56e")

soup = BeautifulSoup(path_to_scrape, "html.parser")
weather = soup.find_all("span", attrs={"class": "TodayDetailsCard--feelsLikeTempValue--8WgHV"})
print(weather)