#
# Basic crawling tools.
# Used to grab links, html and other basic stuff.

import urllib.request
from bs4 import BeautifulSoup

# Basic function that get the links from a webpage. Unless it's a specific 
# case, it's nearly always better to use getLinksFromUrlAndAddHttp() which
# is nearly the same (but translate relative urls to absolute ones). 

def getLinksFromUrl(url):
	with open("links2.txt", "w") as file:
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response)
		for i in soup.find_all('a', href = True):
			file.write(i['href'] + '\n')

# Improved version that get links but also translate them into absolute urls.

def getLinksFromUrlAndAddHttp(url):
	with open("links.txt", "w") as links:
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response, "lxml")
		for i in soup.find_all("a", href = True):
			if i['href'].startswith('h'):
				links.write(i['href'] + "\n")
			elif i['href'].startswith('/'):
				links.write(url + i['href'] + "\n")
			else:
				links.write(i['href'] + '\n')

# Pretty self explanatory. Get the robots.txt file if it exists.
# To be used later (to write : polite and impolite mode)

def getRobotsTxt(url):
	with open("robots.txt", "w") as robotsTxt:
		response = urllib.request.urlopen(url + "/robots.txt")
		soup = BeautifulSoup(response, "lxml")
		robotsTxt.write(soup.get_text())

# Download an html page and save it in an htlm file.
# Amelioration to write : Save the results as different file names.

def download_html(url):
	with open("file.html", "w") as file_html:
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response)
		file_html.write(soup.prettify())

# Download an html page and save it as txt 

def download_html_as_txt(url):
	with open("file.txt", "w") as file_txt:
		response = urllib.request.urlopen(url)
		soup = BeautifulSoup(response)
		file_txt.write(soup.prettify())

# ========================================================================
# TO DO LIST :
# 
# Function that get links from a file. To be used to crawl the next pages.
#
# def getLinksFromFile(file):
# ========================================================================
# 
# Function that grab the email adresses from a page.
#
# def getMail (url):
# 
# regex = [a-zA-Z0-9\._+]+@[a-z]+\.[a-z]{3}
#
# How can I get the mail adresses that are written like this ?:
# "someone [at] mail.com" AND "someone at mail.com"
# ========================================================================

"""
Working notes:
=========
getRobotsTxt():
- Deux manieres de proceder. Avec BeautifulSoup ou sans.
	Sans bs:
		response = urllib.request.urlopen(url + "/robots.txt")
		robotsTxt.write(response.read())
		==> retourne un fichier non mis en forme avec l'ensemble des champs sur une ligne.
	Avec bs:
		response = urllib.request.urlopen(url + "/robots.txt")
		soup = BeautifulSoup(response, "lxml")
		robotsTxt.write(str(soup.prettify()))
		==> mise en forme ( avec prettify() de BeautifulSoup + retransforme en string avec str() 
		mais ajoute des balise <html><body><soup>)

		Idem mais avec :
		robotsTxt.write(soup.get_text())
		==> Fonctionne bien. Mise en forme + pas de balises inutiles.
"""
