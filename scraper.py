from bs4 import BeautifulSoup
import requests

url = "https://hargapetrol.my/malaysia-petrol-prices-list.html"
headers = {'user-agent': 'my-agent/1.0.1'}

#Scrape the data
soup = BeautifulSoup(requests.get(url, headers=headers).text)
start_dates = soup.findAll(lambda tag: tag.name=='div' and tag.has_attr('itemprop') and tag['itemprop']=="validFrom")
ron95s = soup.findAll('div',{"class": "ron95"})
ron97s = soup.findAll('div',{"class": "ron97"})
diesels = soup.findAll('div',{"class": "diesel"})

#Create a CSV
with open('fuel.csv', 'w') as f:
    f.write("Date,Ron95,Ron97,Diesel\n")
    for date,ron95,ron97,diesel in zip(start_dates,ron95s,ron97s,diesels):
        f.write(date.text + "," + ron95.text + "," + ron97.text + "," + diesel.text + "\n")