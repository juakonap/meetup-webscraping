import requests
from bs4 import BeautifulSoup
import config as Configuration

link = Configuration.url_base + 'w3-article-118613.html'

r = requests.get(link); r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, features='html.parser')


links = [x.find('a')['href'] for x in soup.find('div',{'class':' cid-912 aid-118613'}).find_all('p')]

print(links)