import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def scroll_to_bottom(driver, pause_time):
    script_height = "return document.body.scrollHeight"
    script_scroll = "window.scrollTo(0, document.body.scrollHeight);"
    last_height = driver.execute_script(script_height)

    while True:
        driver.execute_script(script_scroll)
        time.sleep(pause_time)
        new_height = driver.execute_script(script_height)
        if new_height == last_height:
            break


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
url = "https://www.realtor.ca/map#view=list&Sort=6-D&GeoIds=g30_c3nfkdtg&GeoName=Calgary%2C%20AB&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD"
driver.get(url)
input('Click me!')

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

    scroll_to_bottom(driver, pause_time = 0.5)
    button = driver.find_element('xpath', '//*[@id="ListViewPagination_Bottom"]/div/a[3]')
    button.click()
    time.sleep(5)

