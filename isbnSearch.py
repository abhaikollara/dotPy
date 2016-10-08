from bs4 import BeautifulSoup
import requests
import webbrowser

ch = raw_input("1. ISBN 2.Name (1/2) : ")
ch = int(ch)
try:
	if ch==1:
		isbn = raw_input("Enter ISBN : ")
		res = requests.get("http://www.isbnsearch.org/isbn/" + str(isbn))
		res.raise_for_status()
		soup = BeautifulSoup(res.text,"lxml")
		info = soup.select('.bookinfo h2')
		print info[0].text
	elif ch==2:
		text = raw_input("Enter search term : ")
		res = requests.get("http://www.isbnsearch.org/search?s="+"+".join(text.split()))
		soup = BeautifulSoup(res.text,"lxml")
		books = soup.select('li h3')
		isbns = soup.select('li .isbnleft')
		for x,y in zip(books,isbns):
			print x.text,"-",y.text[9:]
	else:
		print "Invalid choice !"
except Exception as exc:
	print("Houston, we have a problem ! : %s" %(exc))