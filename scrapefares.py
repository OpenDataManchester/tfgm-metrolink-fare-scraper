from bs4 import BeautifulSoup
import requests

with open("metstopperms.csv") as f:
    for stopcombo in map(str.f):
        url = 'https://beta.tfgm.com/public-transport/tram/ticket-prices/{}'.format(stopcombo)
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data)

        with open('parseddata.txt', 'a') as t:
            for price in soup.find_all('li', {'class': 'ticket-info'}):
                t.write(str(stopcombo) + ',' + str(price.h4.text) + ',' + str(price.p.text) + '\n')

