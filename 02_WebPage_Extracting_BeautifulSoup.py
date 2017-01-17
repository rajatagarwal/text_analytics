"""
Finally, choose a remote webpage and extract key text content from it. 
Install the packages you need and then parse it using BeautifulSoup. 
Try to get to a point where you can extract one of its XML/HTML parts (e.g., title, summary, body)
"""

import nltk, ssl, urllib, urllib.request, bs4

# Bypass SSL
try:
	_create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
	# Legacy Python that doesn't verify HTTPS certificates by default.
	pass
else:
	# Handle target environment that doesn't support HTTPS verification
	ssl._create_default_https_context = _create_unverified_https_context

# Actual Program begins here
url = 'https://en.wikipedia.org/wiki/Morro_Jable_Lighthouse'
urllib.request.urlopen(url)
rawhtml = urllib.request.urlopen(url).read()
print("Raw HTML: ")
print("===================================================================================")
print(rawhtml)

soup = bs4.BeautifulSoup(rawhtml)
title = soup.title
body = soup.body.get_text(strip = True)
p = soup.body.p.get_text(strip = True)

print("Title is: ")
print("===================================================================================")
print(title)

print("Body is: ")
print("===================================================================================")
print(body)


print("First para in body is: ")
print("===================================================================================")
print(p)



