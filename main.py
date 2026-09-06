from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("URL")
google_form = os.getenv("GOOGLE_FORM")
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

listing_links = soup.find_all(name="a", class_="property-card-link")
links = [link.get("href") for link in listing_links]


all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.get_text().split("+")[0] for price in all_prices]


addresses = soup.find_all(name="address")
address = [ad.getText(strip=True) for ad in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(address)):
    driver.get(google_form)

    sleep(2)
    address_ele = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_ele = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_ele = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    sleep(2)

    address_ele.send_keys(address[n])
    price_ele.send_keys(prices[n])
    link_ele.send_keys(links[n])

    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    sleep(2)


