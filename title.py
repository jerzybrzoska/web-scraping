#!/usr/bin/python3
#The script asks you for the address of the webpage in question and returns its title.
#Because of malware, popups, or other reasons you may want to get the title of a web page without visiting it.

import requests
from bs4 import BeautifulSoup

url = input("What is the address of the  web page in question?")

response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)

