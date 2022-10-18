from bs4 import BeautifulSoup
import csv

with open('MLS® & Real Estate Map _ REALTOR.ca.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, features='lxml')
divs = soup.find_all('div', class_='listingCard card')

for div in divs:
    a = div.find('a', class_='blockLink listingDetailsLink')
    href = a.get('href')
    data = div.find('a').get('data-value')
    with open('data.csv', 'a', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow([data, href])




