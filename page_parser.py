from bs4 import BeautifulSoup

with open('test_house.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, features='lxml')

data = {}

divs = soup.find_all('div', class_='propertyDetailsSectionContentSubCon')
for div in divs:
    labels = div.find_all('div', class_='propertyDetailsSectionContentLabel')
    values = div.find_all('div', class_='propertyDetailsSectionContentValue')
    # zip
    for label, value in zip(labels, values):
        data[label.text] = value.text

print(data)

price = soup.find('div', id='listingPriceValue').text
adress = soup.find('div', class_='listingTopDetailsLeft').text

print([price, adress, data])
