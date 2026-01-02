
import requests
from bs4 import BeautifulSoup


def web_scraped():
    url = "https://pennytrain.github.io/universityproj/index.html"
    response = requests.get(url)
    response.raise_for_status()  # will raise for non-200 status codes
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the last <p class="text"> block
    address_block = soup.find_all("p", class_="text")[-1]
    lines = [span.get_text(strip=True) for span in address_block.find_all("span")]

    name = lines[0]
    street = lines[1]
    city_postcode = lines[2]
    phone = lines[3].replace("Phone:", "").strip()

    return (
        f"\nCONTACT US\n"
        f"{name}\n"
        f"{street}\n"
        f"{city_postcode}\n"
        f"{phone}\n"
    )
