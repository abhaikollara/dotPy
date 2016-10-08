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

# i=0

rollList = [12150000,12150076,12150002,12150003,12150004,12150005,12150006,12150077,12150008,12150009,12150010,12150011,12150012,12150013,12150078,12150014,12150015,12150016,
12150017,12150018,12150020,12150079,12150021,12150022,12150023,12150024,12150080,12150025,12150026,12150027,12150028,12150029,12150081,12150030,12150082,12150031,
12150032,12150033,12150034,12150083,12150035,12150036,12150037,12150038,12150039,12150040,12150041,12150042,12150043,12150044]

for y in rollList:
	td = getResult(y)

	fo = open("results.csv","a")

	fo.write(td[0])
	fo.write(",")
	fo.write(td[1])
	fo.write(",")

	for i in range(10,55,4):
		fo.write(td[i][:-3])
		fo.write(",")

	fo.write("\n")
	fo.close

	print y,"Done"