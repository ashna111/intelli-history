from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests
url = "https://medium.com/ninjaconcept/interactive-dynamic-force-directed-graphs-with-d3-da720c6d7811"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
all_paragraphs = soup.find_all("p")
content = []
for x in all_paragraphs:
#     print(x.get_text()+"\n")
    content.append(x.get_text())

from gensim.summarization import keywords

text=""
for i in content:
	text=text+i

z=keywords(text).split('\n')
print(z)
