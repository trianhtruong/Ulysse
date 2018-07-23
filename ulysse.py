# Ulysse v0.1
# Let's go !

from bs4 import BeautifulSoup
import urllib.request
import basictools


# Test sur get_text()
def test_sur_get_text(url):
	with open("result_test_get_text.txt", "w") as file:
		html = urllib.request.urlopen(url)
		bsObj = BeautifulSoup(html, "lxml")
		result = bsObj.get_text()
		file.write(result)

def main():
	url = input("Enter the starting url: ")
	basictools.getRobotsTxt(url)
	basictools.getLinksFromUrlAndAddHttp(url)
	basictools.download_html(url)
	basictools.download_html_as_txt(url)
#	test_sur_get_text(myUrl)
	

main()

