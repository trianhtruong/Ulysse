# Ulysse v0.1
# Let's go !

from bs4 import BeautifulSoup
import urllib.request
import basictools


def erase(file):
	with open(file, "w") as f:
		f.write("")

# This function get the first link inside 'links.txt' - it's the next link to
# crawl. Then, remove it from the 'links.txt' file so that the second line
# become the first and so on.
def crawl(file):
	with open(file, "r") as f1:
		# Use the iterator to get the first line in the file.
		# The iterator is now after the first line.
		urltocrawl = next(f1)
		with open("links.txt.temp", "w") as f2:
			# Read from the iterator position, therefore ignoring the first
			# line and save what's read into a temp file.
			f2.write(f1.read())
	# Simply overwrite the first file with the temp file. Now all line have 
	# gone one line up and the first line is deleted (it's in 'urltocrawl')
	with open("links.txt.temp", "r") as f2:
		with open(file, "w") as f1:
			for line in f2:
				f1.write(line)
	# We keep logging visited urls. See lines 54 / 55.
	with open("visited.txt", "a") as v:
		v.write(urltocrawl)			
	return urltocrawl	

# Used to separate the links obtained from different pages in 'links.txt'
def drawline(file):
	with open(file, "a") as f:
		f.write("-------------------------------\n")

def main():
	# Start by erasing the old links from previous crawls.
	# Save them if you want to keep them.
	erase("links.txt")
	erase("links.txt.temp")
	erase("visited.txt")

	url = input("Enter the starting url: ")
	depth = int(input("How many links do you want to crawl ?:"))

	# saving the value of the starting url to transform relative urls in
	# absolute ones.
	# Only work as long as the crawler stays on the same domain...
	domain = url

	# Get the links from the starting page and save them inside "links.txt"
	print("Visiting " + url)
	basictools.getLinksFromUrlAndAddHttp(url, domain)

	# "visited.txt" serves as a log of visited links.
	# The number of visited links should be equal to the value of 'depth'
	with open("visited.txt", "a") as v:
		v.write(url)
	depth -=1

	while(depth > 0):
		# Serves as a visual limit beetwen the gathered links
		# So we can tell which links come from which url a little easier
		# Can be commented out if the user has no use for that.
		drawline("links.txt")

		# The part that allow the crawler to explore.
		url = crawl("links.txt")
		print("Visiting " + url)
		basictools.getLinksFromUrlAndAddHttp(url, domain)
		depth -=1

		# Additionnal capacities. Just uncomment if you need to download html
		# grab the robots.txt or something else.
		# Careful for now. The errors are not handled yet.

		#basictools.getRobotsTxt(url)
		#basictools.getLinksFromUrlAndAddHttp(url)
		#basictools.download_html(url)
		#basictools.download_html_as_txt(url)


main()


