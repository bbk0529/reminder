import requests
from bs4 import BeautifulSoup

def get_value(link):
	page=requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	result=soup.find(class_="BNeawe iBp4i AP7Wnd").get_text()
	print(result)


currencies=["euro","dollar","JPY","CNY"]
for currency in currencies :
	link="https://www.google.de/search?q=1" + currency + "+to+krw&oq=1" + currency + "+to+krw"
	print(link)
	get_value(link)

#get_value(link)
# link=[]
# link.append(link1)
# link.append(link2)

# for l in link :
# 	get_value(l)
