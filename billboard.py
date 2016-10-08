from bs4 import BeautifulSoup
import requests

try:
	mainpage = requests.get("http://www.billboard.com/charts")
	i=1		#To show serial numbers
	j=1
	try:
		mainpage.raise_for_status()
		soup = BeautifulSoup(mainpage.text,"lxml")
		titles = soup.select(".field-content a")
		for x in titles:
			print x.text
		search = raw_input("Enter search term : ")
		search = search.lower()
		for x in titles:
			if(x.text.lower().find(search) != -1):
				print str(i).ljust(2," "),x.text.strip()
			i+=1
		ch = raw_input("Enter choice : ")
		ch = int(ch)
		url = titles[ch-1].get('href')

		url = "http://www.billboard.com"+url
		res = requests.get(url)
		soup2 = BeautifulSoup(res.text,"lxml")
		sList = soup2.select(".chart-row__title .chart-row__song")
		aList = soup2.select(".chart-row__title .chart-row__artist")

		print "-----------------------------------------------"
		print titles[ch-1].text
		print "-----------------------------------------------"
		for x,y in zip(sList,aList):
			print str(j).ljust(2," "),x.text.ljust(30," "),"\t",y.text.strip()
			j+=1
	except Exception as exc:
		print ("Error : %s" %exc)
except:
	print "Error"