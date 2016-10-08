import requests
from bs4 import BeautifulSoup


def getResult(rNo):
	url = "http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/Result_Declaration/display_sup_result"

	formData = {
		
		'regno' : str(rNo),
		'deg_name' : "B.Tech",
		'semester' : "1&2",
		'month' : "May",
		'year' : "2015",
		'result_type' : "Regular",
		'date_time' : "2016/05/20 11:58:18.412 GMT+0530"
	}

	response = requests.post(url,formData)

	soup = BeautifulSoup(response.text,"lxml")

	li = soup.select("td")



	td=[]

	for x in li:
		td.append(x.text.strip())

	return td

num = raw_input("Enter register number : ")

t = getResult(num)

print ""
print "Name :",t[1]
print "Branch :",t[3]
print ""

print "Subject Code".ljust(15," "),"Subject".ljust(70," "),"Marks".ljust(9," "),"Status"
for i in range(9,54,4):
	print t[i-1].ljust(15," "),t[i].ljust(70," "),t[i+1].ljust(9," "),t[i+2]