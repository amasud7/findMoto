from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def build_url(loc):
    # Setup Search Parameters
    location = loc + '/'
    min_price = 1000
    max_price = 6000
    max_mileage = 5000
    min_year = 2015

    url = f'https://www.facebook.com/marketplace/{location}vehicles?minPrice={min_price}&maxPrice={max_price}&maxMileage={max_mileage}&minYear={min_year}&sortBy=creation_time_descend&topLevelVehicleType=motorcycle&exact=false'

    return url


def chrome_driver():
    # Configure Driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--headless")

    return webdriver.Chrome(options=chrome_options)


def extract_mileage(text):
    match = re.search(r'(\d+(\.\d+)?)K?', text)  # Capture numbers and optional decimal + 'K'
    if match:
        num = float(match.group(1))  # Extract matched number
        if 'K' in text:
            return int(num * 1000)  # Convert 'K' to full numerical value
        return int(num)
    return None  # Return None for outliers


def get_listings(search_url):
    # Initialize Driver
    driver = chrome_driver()

    # Go to URL
    driver.get(search_url)

    listings = []
    # Locate the info, img, and listing link using XPath
    for i in range(1, 10+1):
        listing_info = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[{i}]/div/div/span/div/div/div/div/a/div/div[2]')
        listing_img = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[{i}]/div/div/span/div/div/div/div/a/div/div[1]/div/div/div/div/div/img')
        listing_link = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[5]/div/div[2]/div[{i}]/div/div/span/div/div/div/div/a')

        text = listing_info.text.split('\n')
        img_src = listing_img.get_attribute('src')
        link = listing_link.get_attribute('href')

        # In the case of a price reduction, removes previous price
        if len(text) > 4:
            text.pop(1)


        data = {
            "Price": int(text[0].replace("$", "").replace(",", "")),
            "Name": text[1],
            "Location": text[2],
            "Mileage": extract_mileage(text[3]),
            "Image": img_src,
            "Link": link
            }

        listings.append(data)
    
    driver.quit()

    return listings
