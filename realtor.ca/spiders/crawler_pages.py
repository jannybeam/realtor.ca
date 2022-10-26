import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

def parse_page(soup):
    data = {}

    divs = soup.find_all('div', class_='propertyDetailsSectionContentSubCon')
    for div in divs:
        labels = div.find_all('div', class_='propertyDetailsSectionContentLabel')
        values = div.find_all('div', class_='propertyDetailsSectionContentValue')
        # zip
        for label, value in zip(labels, values):
            data[label.text] = value.text

    price = soup.find('div', id='listingPriceValue').text
    adress = soup.find('div', class_='listingTopDetailsLeft').text

    print([price, adress, data])
    return [price, adress, data]

with open('pages.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    for i, row in enumerate(read):
        if i == 0:
            continue
        driver.get(row[1])
        soup = BeautifulSoup(driver.page_source, features='lxml')
        meta = soup.find_all('meta')[0]
        if meta.get('name') == 'ROBOTS':
            input('Please press when capcha solved: ')
        time.sleep(4)

        with open('houses.csv', 'a', newline = '') as f:
            house_data = parse_page(soup)
            writer = csv.writer(f)
            writer.writerow(house_data + row)


