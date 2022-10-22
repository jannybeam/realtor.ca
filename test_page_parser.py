import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import sleep

# from requests_html import HTMLSession
# s = HTMLSession()
# response = s.get('https://www.realtor.ca/real-estate/24993633/266048-16-street-e-rural-foothills-county')
# response.html.render(
#     wait=8,
#     timeout=10,
#     sleep=4
# )
# with open('item.xml', 'wb') as file:
#     file.write(response.html.raw_html)


var = UserAgent().chrome
url = "https://www.realtor.ca/real-estate/24993633/266048-16-street-e-rural-foothills-county"
response = requests.get(url).text
print(response)

soup = BeautifulSoup(response, features='lxml')

price = soup.find('div', class_='listingPriceValue')
adress = soup.find('h1', class_='unsetH1')
summary = soup.find_all('div', class_='propertyDetailsSectionContentValue')

# property_type = soup.find('div', class_='propertyDetailsSectionContentValue').text
# land_size = soup.find('div', class_='propertyDetailsSectionContentValue').text
# building_type = soup.find('div', class_='propertyDetailsSectionContentValue').text
# year = soup.find('div', class_='propertyDetailsSectionContentValue').text
# storeys = soup.find('div', class_='propertyDetailsSectionContentValue').text

building_land = soup.find_all('div', class_='propertyDetailsValueSubSectionCon')
rooms = soup.find_all('div', class_='propertyDetailsRoomContent')
print(building_land)


# FOR ALL CARDS
data - []
for page in range(1, 51):
    print(page)

    url = "https://www.realtor.ca/map#ZoomLevel=4&Center=54.920828%2C-99.316406&LatitudeMax=67.13156&LongitudeMax=-46.58203&LatitudeMin=37.43125&LongitudeMin=-152.05078&view=list&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=FXUSDCAD"
    response = requests.get(url).text
    sleep(3)
    soup = BeautifulSoup(response, features='lxml')

    houses = soup.find_all('div', class_='largeListingCardCon')
    len(houses)

    for house in houses:
        url = "https://www.realtor.ca"
        # ???

    data.append(# ???)
