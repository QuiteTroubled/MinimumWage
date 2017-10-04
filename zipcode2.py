#Zip Code
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from openpyxl import Workbook
wb = Workbook()
#https://openpyxl.readthedocs.io/en/default/

file = open("plaintexttxt.txt","w")


print "Captitalise the first letter of each word. Replace spaces with \'-\'"
print "Valid:San-Francisco"
print "Valid:California"
print "Invalid san francisco"
print "Washington DC is city:Washington state:District-of-Columbia"
zipcode = "Null"
while True:
	try:
		city = raw_input("City>")
		state = raw_input("State>")	
	
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
		length = len(zipcode)
		x = 0
		while True:
			print zipcode[x]
			
			if x == length - 1:
				break
			x+=1
	
		file.write(city +"\n"+ state)
	
		for entry in zipcode:
		  file.write(entry)
		break
	
	except:
		print "Invalid City and/or State"



print "Done"
#<div class="discount_final_price">$29.99</div>