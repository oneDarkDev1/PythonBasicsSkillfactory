Book Scraper (Books to Scrape)

This project is a simple web scraper written in Python that extracts book information from Books to Scrape.
It collects details such as:
    Title
    Rating (converted into stars ⭐)
    Price
    Availability
and saves the results into an Excel file (books.xlsx).

🚀 Features

Scrapes all pages from books.toscrape.com.
Extracts book details using BeautifulSoup.
Converts textual ratings (One, Two, etc.) into star symbols (★).
Stores results in an Excel file using pandas.

🛠️ Requirements

Install the dependencies before running the script:
pip install requests beautifulsoup4 pandas openpyxl