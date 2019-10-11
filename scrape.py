from requests import get
import urllib.request
from BeautifulSoup import BeautifulSoup

#Grab HTML page
def grabWebPage(url)
	str(url)
	response = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
	html = response.content 
	print(html)
	
grabWebPage(https://www.sports-reference.com/cfb/coaches/urban-meyer-1.html)

#HTML parsing library
#soup = BeautifulSoup(html)
#print soup.prettify()

/Users/nicknovak/Desktop/first-web-scraper-master/Code/scrape.py