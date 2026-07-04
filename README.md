
# Amazon Clothes Scraper

A simple Python script that searches Amazon for a product category (clothes, by default), pulls the **product name** and **price** from the search results page, and saves everything into a clean CSV file you can open in Excel or Google Sheets.

![Person shopping online](https://images.pexels.com/photos/230544/pexels-photo-230544.jpeg)
*Example of the everyday use case this script automates: instead of manually browsing and copying prices, the script does it for you in seconds.*

## What it does

1. Sends a request to an Amazon search results URL, disguised as a real browser (via a custom `User-Agent` header) so the request isn't blocked.
2. Parses the HTML with **BeautifulSoup** to find every product listing on the page.
3. Extracts the **name** and **price** of each product.
4. Writes the results to `amazon_clothes.csv`.
5. Prints a summary of how many items were saved.

## Example output

Once the script runs, you'll get a CSV file that looks like this when opened in a spreadsheet app:

![Example spreadsheet CSV output](https://cdn.pixabay.com/photo/2018/03/07/23/48/spreadsheet-3206026_1280.jpg)
*Illustrative example — the actual file will contain real product names and prices from your search.*

| Name | Price |
|------|-------|
| Men's Cotton Crew T-Shirt | $14.99 |
| Women's Slim Fit Jeans | $29.99 |
| Unisex Fleece Hoodie | $22.50 |

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Open `amazon_scraper.py` and change the `url` variable to whatever Amazon search you want to scrape:

   ```python
   url = "https://www.amazon.com/s?k=clothes"
   ```

2. Run the script:

   ```bash
   python amazon_scraper.py
   ```

3. Check your project folder for `amazon_clothes.csv` — it will contain the scraped names and prices.

## Project structure

```
.
├── amazon_scraper.py     # Main script
└── amazon_clothes.csv    # Generated after running (output file)
```

## Limitations & notes

- **Amazon's HTML changes often.** If the script stops finding results, Amazon likely updated its page structure — the CSS selectors (`div[data-component-type='s-search-result']`, etc.) will need updating.
- **Only scrapes one page.** It grabs whatever loads on the first search results page; it doesn't paginate through more results.
- **No error handling for blocked/failed requests.** If Amazon returns a CAPTCHA or blocks the request, the script will run but the CSV will end up empty.
- **Rate limiting is your responsibility.** Sending too many requests quickly can get your IP temporarily blocked.
- **Legal/ethical note:** Scraping Amazon may violate their [Conditions of Use](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088), which prohibits automated data collection without permission. Use this script responsibly, for personal/educational purposes, and check current terms before scraping at scale.

## Possible improvements

- Add pagination support to scrape multiple pages of results.
- Add retry logic and error handling for failed requests.
- Store data in a database instead of (or in addition to) CSV.
- Add product ratings, review counts, and image URLs to the output.
- Use rotating proxies/User-Agents to reduce the chance of being blocked.
