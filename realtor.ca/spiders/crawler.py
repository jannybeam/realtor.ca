import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException


def scroll_to_bottom(driver, pause_time):
    # script_height = "return document.body.scrollHeight"
    # script_scroll = "window.scrollTo(0, document.body.scrollHeight);"
    # # last_height = driver.execute_script(script_height)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause_time)


def parse_price_range(driver):
    while True:
        soup = BeautifulSoup(driver.page_source, features='lxml')
        divs = soup.find_all('div', class_='listingCard card')

        for div in divs:
            a = div.find('a', class_='blockLink listingDetailsLink')
            href = a.get('href')
            data = div.find('a').get('data-value')
            with open('../data/data.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                print([data, href])
                writer.writerow([data, href])

        scroll_to_bottom(driver, pause_time=0.5)
        
        button = driver.find_element('xpath', '//*[@id="ListViewPagination_Bottom"]/div/a[3]')
        if button.get_attribute('disabled'):
            return

        try:
            button.click()
        except ElementNotInteractableException:
            return

        time.sleep(3)


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
start = 16
for i in range(start, 80):
    min_price = i*25000
    max_price = (i+1)*25000
    url = f"https://www.realtor.ca/map#ZoomLevel=10&Center=51.028188%2C-114.086920&LatitudeMax=51.35738&LongitudeMax=-113.44010&LatitudeMin=50.69664&LongitudeMin=-114.73374&view=list&Sort=1-D&PGeoIds=g30_c3nfkdtg&GeoName=Calgary%2C%20AB&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&PriceMin={min_price}&PriceMax={max_price}&Currency=CAD"
    # url = 'https://www.realtor.ca/map#ZoomLevel=10&Center=51.028188%2C-114.086920&LatitudeMax=51.35738&LongitudeMax=-113.44010&LatitudeMin=50.69664&LongitudeMin=-114.73374&view=list&Sort=1-D&PGeoIds=g30_c3nfkdtg&GeoName=Calgary%2C%20AB&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&PriceMin=125000&PriceMax=150000&Currency=CAD'
    # For some reasons requestiing ones doesn't work
    driver.get(url)
    time.sleep(2)
    driver.get(url)
    if i == start:
        input('Click me!')
    parse_price_range(driver)
    time.sleep(3)