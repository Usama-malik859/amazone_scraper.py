import requests
from bs4 import BeautifulSoup
import csv

# 1. Put the Amazon search URL here (example: clothes search)
url = "https://www.amazon.com/s?k=clothes"

# 2. Amazon blocks requests that don't look like a real browser,
#    so we pretend to be one
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}

# 3. Download the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 4. Find each product box on the search results page
products = soup.select("div[data-component-type='s-search-result']")

# 5. Grab the name and price from each product
rows = []
for product in products:
    name_tag = product.select_one("h2 span")
    price_tag = product.select_one("span.a-price > span.a-offscreen")

    name = name_tag.get_text(strip=True) if name_tag else None
    price = price_tag.get_text(strip=True) if price_tag else None

    if name and price:
        rows.append([name, price])

# 6. Save results to a CSV file
with open("amazon_clothes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price"])
    writer.writerows(rows)

print(f"Done! Saved {len(rows)} items to amazon_clothes.csv")
