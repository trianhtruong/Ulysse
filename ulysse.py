# Ulysse v0.1

from bs4 import BeautifulSoup
import urllib.request
import basictools
import menu

def erase(file):
	with open(file, "w") as f:
		f.write("")

# This function get the first link inside 'links.txt' then, remove it from
# the 'links.txt' file so that the second line become the first and so on.
def crawl(file):
	with open(file, "r") as f1:
# Use the iterator to get the first line in the file. The iterator is now 
# after the first line.
		urltocrawl = next(f1)
		with open("links.txt.temp", "w") as f2:
			# Read from the iterator position, ignoring the first line.
			f2.write(f1.read())
# Overwrite the first file with the temp file. Now all line have 
# gone one line up and the first line is deleted (it's in 'urltocrawl')
	with open("links.txt.temp", "r") as f2:
		with open(file, "w") as f1:
			for line in f2:
				f1.write(line)

	with open("visited.txt", "a") as v:
		v.write(urltocrawl)			
	return urltocrawl

def drawline(file):
	with open(file, "a") as f:
		f.write("-------------------------------\n")

def initialize():
	erase("links.txt")
	erase("links.txt.temp")
	erase("visited.txt")

	url = input("\n" + "Enter the starting url: ")
	depth = int(input("\n" + "How many links do you want to crawl ?: "))

# saving the value of the starting url to transform relative urls in
# absolute ones. Only works as long as the crawler stays on the same domain
	domain = url
	with open('domain.txt', 'w') as d:
		d.write(domain)
	return url, depth, domain

def visitFirstPage(url, domain):
# Get the links from the starting page and save them inside 'links.txt'
		print("\n" + "Visiting " + url + "\n")
		basictools.getLinksFromUrlAndAddHttp(url, domain)

		# "visited.txt" serves as a log of visited links.
		# The number of visited links should be equal to the value of 'depth'
		with open("visited.txt", "a") as v:
			v.write(url)

def main():
	choice = menu.display()
	
# New crawl. Start by erasing the old files.	
	if choice == '1':
		url, depth, domain = initialize()
		visitFirstPage(url, domain)
		depth -=1

	elif choice == '2':
		with open('domain.txt', 'r') as d:
			domain = d.readline()
		print ("Domain : " + domain)
		depth = int(input("\n" + "How many links do you want to crawl ?: "))
	
	else :
		print("Something wrong happened.")

	while(depth > 0):
		# Serve as a separator between visited pages.
		drawline("links.txt")

		# The part that allow the crawler to explore.
		url = crawl("links.txt")
		print("Visiting " + url)
		basictools.getLinksFromUrlAndAddHttp(url, domain)
		depth -=1

		# Additionnal capacities. Just uncomment to use.
		# Errors not handled, yet.

		#basictools.getRobotsTxt(url)
		#basictools.getLinksFromUrlAndAddHttp(url)
		#basictools.download_html(url)
		#basictools.download_html_as_txt(url)

main()
