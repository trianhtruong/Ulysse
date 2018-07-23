# Ulysse v0.1
# Let's go !

from bs4 import BeautifulSoup
import urllib.request
import basictools

def main():
	url = input("Enter the starting url: ")
	basictools.getRobotsTxt(url)
	basictools.getLinksFromUrlAndAddHttp(url)
	basictools.download_html(url)
	basictools.download_html_as_txt(url)

main()

