import requests
from bs4 import BeautifulSoup


def web_scraped():
    url = "https://pennytrain.github.io/universityproj/index.html"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        address_block = soup.find_all("p", class_="text")[-1]
        lines = [
            span.get_text(strip=True)
            for span in address_block.find_all("span")
            ]

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

    except requests.exceptions.RequestException:
        return "Error: Unable to connect to the website."

    except (IndexError, AttributeError):
        return "Error: Website structure has changed."
