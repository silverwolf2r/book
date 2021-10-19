#basically want to have a list of websites and we will google search for a book on these websites.
#The search would be title site:onlinereadfreenovel.com
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import isbnlib

#----------------------------------------------------
#Finding the book title
#----------------------------------------------------
gtitle = input("What is the Title of the Book: ")
author = input("Authors Name: ")
book = isbnlib.goom(gtitle + ' ' + author) 
isbn1 = book[0]
isbn = str(isbn1)
# I want the first 28 characters of str isbn
isbn = isbn[13:26]
book = isbnlib.meta(isbn)
title = book['Title']
author = book['Authors']
print('\n')	
print('\n')	
print('Title: ' + str(title) + '\n' + 'Author: ' + str(author))
print('\n ISBN: ' + isbn)

#----------------------------------------------------
#Formulate the google query and results
#----------------------------------------------------
resultinglinks = []
searching = str(title) + ' "Page 1" site:'
x = 0
links = ["onlinereadfreenovel.com", "readonlinefreenovel.com", "novel80.com", "thefreeonlinenovel.com", "readonlinefreebook.com", "lovefreenovels.com", "novel122.com", "www.topbooks2019.com" ]
for link in links:
	query = searching + link
	result = search(query , num_results=0)
	resultinglinks.append(result)


for results in resultinglinks:
	x = x + 1
	linkresults = str(x) + " " + str(results)
	print(linkresults)
	
#---------------------------------------------------
#Use the chosen link to download
#---------------------------------------------------	
chosenlink = input("Which link would you like to download? (enter in a number) ")
chosenlink = int(chosenlink) - 1
link = (resultinglinks[chosenlink])
link = str(link).replace("'","")
link = str(link).replace("[","")
link = str(link).replace("]","")
#for each link I need to format a way to download it from that link no matter how odd the link is





#DOWNLOAD INFORMATION FOR EACH LINK RIGHT NOW
#link1 onlinereadfreenovel.com
#-------------------------------------------------textid, Page_next
if chosenlink == 0:

	textid = "textToRead"
	Nextpage = "page_next"
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find(id=textid)
		text = akt.text 
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in soup.find_all(Nextpage,href=True):
			print(links)
			link = links


#link2 readonlinefreenovel.com
#-------------------------------------------------search by classs=content, next-page
elif chosenlink == 1:

	textid = "p"
	Nextpage = "next-page"
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="content")
		text = akt.text
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in soup.find_all(Nextpage,href=True):
			print(links)
			link = links
		
		

#link3 novel80.com 
#-------------------------------------------------search by chapter-content, search for Next page		
elif chosenlink == 2:

	textid = "p"
	Nextpage = "Next Page"
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="chapter-content")
		text = akt.text
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in soup.find_all(Nextpage,href=True):
			print(links)
			link = links
		
		
#link4 thefreeonlinenovel.com	
#Needs Revision
#-------------------------------------------------textid <td>, linksy
elif chosenlink == 3:

	textid = "td"
	Nextpage = "Next Page"
	print('This link needs revision and will most likely break. Feel free to try but eh...')
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	linksyl = link
	linksy = (linksyl[-1])
	linksy = linksyl.replace(linksy, "")
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find(textid)
		text = akt.text
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		
		link = str(linksy) + str(x)
		
#link5 readonlinefreebook.com
#-------------------------------------------------search for class content_novel, search for class of nextpage
elif chosenlink == 4:

	textid = "p"
	res = requests.get(link)
	text = res.text
	soup = BeautifulSoup(text, 'html.parser')
	Nextpage = soup.find_all("div", class_="fa fa-angle-right")
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="content_novel")
		text = akt.text
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in Nextpage:
			print(links)
			link = links

#link6 lovefreenovels.com
#-------------------------------------------------search for text class, search for text
elif chosenlink == 5:

	textid = "text"
	Nextpage = "Next"
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="text")
		text = akt.text 

		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in soup.find_all(Nextpage,href=True):
			print(links)
			link = links
	
#link7 novel122.com
#-------------------------------------------------search by classs=chapter-content-p, search by class btn-blue
elif chosenlink == 6:

	textid = "btn-blue"
	res = requests.get(link)
	text = res.text
	soup = BeautifulSoup(text, 'html.parser')
	Nextpage = soup.find_all("div", class_="next-page")
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="chapter-content-p")
		text = akt.text
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		for links in Nextpage:
			print(links)
			link = links
		
		


#link8 www.topbooks2019.com
#-------------------------------------------------textid <p>, linksy
elif chosenlink == 7:

	textid = "p"
	Nextpage = "Next"
	
	#prep a document for the book to be written too
	tity = ''.join(filter(str.isalpha, title))
	f = open( str(tity) + ".txt", "w") 
	f.write("HERE IS YOUR BOOK:   ")
	f.close()

	#set for how many iterations this will run for
	tfoncode = int(200)
	x = 0
	linksy = link
	while x < tfoncode + 1:
		x = x + 1
		#Get the html from the webpage 
		res = requests.get(link)
		text = res.text
		
		# Take the text and parses the html out so that it is easy to read
		soup = BeautifulSoup(text, 'html.parser')
		title = soup.title.string
		akt = soup.find("div", class_="main")
		text = akt.text 
		
		#Write the page to the document
		startpage = int(x)
		final_product = (str(title) + str(text) )
		fp = final_product # tfontext requires parsing everytime
		f = open( str(tity) + ".txt", "a") # write page to the document
		f.write(fp)
		f.close()
		print(startpage ,"/",tfoncode )
		startpage = startpage + 1
		
		#get the next url rinse and repeat
		link = str(linksy) +  "index_" + str(startpage) + ".html"
