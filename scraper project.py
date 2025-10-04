import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_info():
    i = 1
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    while True:
        base_url = f"https://books.toscrape.com/catalogue/page-{i}.html"

        res = requests.get(base_url)
        if res:
            soup = BeautifulSoup(res.text, "html.parser")
            books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")


            for book in books:
                data = {}
                book_details = book.find("article", class_="product_pod")
                data["name"] = book_details.find("h3").find("a").get("title")
                data["rating"] = "★" * rating_map[book_details.find("p").get("class")[1]]
                data["price"] = book_details.find("p", class_="price_color").get_text(strip=True)[1:]
                data["availability"] = book_details.find("p", class_="instock availability").get_text(strip=True)
                yield data
            i += 1
        else:
            break

result = collect_info()
for record in result:
    df = pd.DataFrame(result)
    df.to_excel("books.xlsx", index=False)