# Data-Entry-Job-Automation

A Python automation script that:

1. Scrapes property addresses, prices, and listing links from a website.
2. Opens a Google Form with Selenium.
3. Enters each listing into the form automatically.

The original project uses BeautifulSoup + Requests for scraping and Selenium for browser automation.

## ✨ Overview

This project collects property listing information from a target website and automatically submits the collected data to a Google Form.

The application extracts:

- Property address
- Property price
- Property listing URL

After scraping the listings, Selenium opens the configured Google Form and submits each property automatically.

## ✨ Features

- Scrapes property listings using BeautifulSoup
- Sends HTTP requests using Requests
- Extracts property addresses, prices, and URLs
- Automatically opens Google Chrome using Selenium
- Fills and submits a Google Form
- Uses environment variables for configuration
- Keeps sensitive configuration out of GitHub

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Requests | Fetch webpage HTML |
| BeautifulSoup | Parse and extract listing data |
| Selenium | Browser automation |
| python-dotenv | Environment variable management |
| Google Forms | Store submitted listings |

## Project structure

```text
property-listing-automation/
├── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9+
- Google Chrome
- A Google Form with fields for address, price, and link
- A listing page whose HTML contains the selectors used by `main.py`

Selenium 4 can generally manage the Chrome driver automatically when the environment supports Selenium Manager.

## Run

```bash
python main.py
```

Chrome will open and the script will submit each scraped listing to the configured Google Form.

## Notes

- Only listings for which all three values are available are submitted.
- The script uses the minimum length of the address, price, and link lists to avoid index errors.
- Respect the target website's terms of service, robots.txt, rate limits, and applicable laws.
- Avoid submitting duplicate listings if the target form does not support deduplication.
