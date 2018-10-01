# Beautiful Soup (Coursera course)
# Uses python3

import urllib.parse, urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter a URL:")

html = urllib.request.urlopen(url, context = ctx).read()

soup = BeautifulSoup(html,"html.parser")

# Example of usage
if __name__ == "__main__":	
	tags = soup("a")
	for tag in tags:
		print(tag.get("href", None))
