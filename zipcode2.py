#Zip Code
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from openpyxl import Workbook
import json
wb = Workbook()
def DumpDict(ZipCode):
	with open(zipcode.json, 'w') as f:
		json.dump(ZipCode, f)	
def FindZipcode(city, state):
	zipcode = "Null"
	url = "http://www.city-data.com/zipmaps/"+city+"-"+state+".html"
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")

	zipcode = soup.find_all("div",{"class": "zip-codes"}) [0].text
	zipcode = str(zipcode)

	print zipcode
	zipcode = zipcode.replace("Z","")
	zipcode = zipcode.replace("i","")
	zipcode = zipcode.replace("p","")
	zipcode = zipcode.replace("c","")
	zipcode = zipcode.replace("o","")
	zipcode = zipcode.replace("d","")
	zipcode = zipcode.replace("e","")
	zipcode = zipcode.replace("s","")
	zipcode = zipcode.replace(":","")						
	zipcode = zipcode.replace(",","|")
	zipcode = zipcode.replace(".","")
	zipcode = zipcode.replace(" ","")
	zipcode = zipcode.split("|")
	StringZipcode = ''.join(zipcode)
	x = 0
	ZipCode = dict()
	ZipCode['0'] = {'City': city,  	'State': state, 'ZipCodes': StringZipcode}
	DumpDict(ZipCode)
FindZipcode('Akron',"Ohio")

#def Start():
#	print "Would you like to add to the dict or read the dict?"
#

#def ReadDict():
#


#<div class="discount_final_price">$29.99</div>