from bs4 import BeautifulSoup
import requests
import re

import os


url = "https://python.langchain.com/en/latest/index.html"
url1 = "https://en.wikipedia.org/wiki/Algorithm"

def get_data(url):
    data = requests.get(url)
    return data.text

def get_links(website_link):
    html_data = get_data(website_link)
    soup = BeautifulSoup(html_data, "html.parser")
    soup.prettify()
    print(soup.find_all('meta'))
    list_links = []
    for link in soup.find_all('a', href=True):
        list_links.append(link["href"])
    return list_links

sub_links = get_links('https://xgboost.readthedocs.io/en/stable/')
print(len(sub_links))
#print(sub_links)

# url = "https://en.wikipedia.org/wiki/Algorithm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print("The href links are :")
# for link in soup.find_all('a'):
#    print(link.get('href'))

# html = '''<a href="https://some_url.com">next</a>
# <span class="class">
# <a href="https://some_other_url.com">another_url</a></span>'''

# soup = BeautifulSoup(html)

# for a in soup.find_all('a', href=True):
#     print("Found the URL:", a['href'])
print('*********************************************************')
url = "https://unisyscorp.sharepoint.com/Pages/InsideUnisys.aspx"
req = requests.get(url)
print(req)
soup = BeautifulSoup(req.text, "html.parser")
print("The href links are :")
for link in soup.find_all('a'):
   print(link.get('href'))