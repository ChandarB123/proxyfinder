import requests
from bs4 import BeautifulSoup
import json

url = 'https://free-proxy-list.net/'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')#.prettify()
proxy_list = soup.find_all('textarea', class_='form-control')[0].get_text()
listproxy = proxy_list.split('\n')[3:-1]

with open('proxylist.txt', 'a') as file:
    for proxy in listproxy:
        proxy = proxy + '\n'
        file.write(proxy)
