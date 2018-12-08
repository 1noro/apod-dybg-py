# VERSION: 20181208a
# By boot1110001. Based on the script of Josh Schreuder (2011)

import os #for home dir syntax
import re #for regex
import urllib2 #to download websites

os.path.expanduser('~') #to get the home user

# FUNCTIONS
def get_page():
	print("Downloading the page to find the image...")
	web_content=urllib2.urlopen('http://apod.nasa.gov/apod/').read()
	# ~ NO HAY IMAGEN HOY
	
def get_page2():
	print("Downloading the page to find the image2...")
	web_content=urllib2.urlopen('http://www.aapodx2.com/').read()
	web_match = re.match(r".*href=\"(.*?)\"><img", web_content)
	
	print(web_match)
	
	if web_match:
		print("Match: "+web_match.group(1))
	else:
		print("No match")
		
	matches = re.finditer(r".*href=\"(.*?)\"><img", web_content)
	print(matches.next().groups())
	print(matches.next().groups())

get_page2()
