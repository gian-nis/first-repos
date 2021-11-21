# Prints out every title on the nytimes homepage

import requests

from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'

result = requests.get(url)  # let requests method yoink url
doc = BeautifulSoup(result.text, "html.parser")
# result.text is to make url a text file i think and the second parameter is the type of parser you're using

titles = doc.find_all(['h3', {'class': 'balancedHeadline'}])
# in the brackets, you're putting the tag that title is listed under i think

for item in titles:
    print(item.text.strip())
    print("---")
# this gets whatever is in titles and takes nothing but the strings
