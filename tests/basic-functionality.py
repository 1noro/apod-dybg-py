# VERSION: 20181208a
# By boot1110001. Based on the script of Josh Schreuder (2011)

import os #for home dir syntax
import re #for regex
import urllib #to download websites
import urllib2 #to download websites
import datetime

os.path.expanduser('~') #to get the home user

today=datetime.datetime.now().strftime("%Y%m%d") #date in format YYYYmmdd

# FUNCTIONS
def get_page1():
	print("Downloading the page to find the image...")
	web_content=urllib2.urlopen('http://apod.nasa.gov/apod/').read()
	patron = re.compile('.*<IMG SRC=\"(.*?)\"')
	matcher = patron.findall(web_content)
	return 'http://apod.nasa.gov/apod/'+matcher[0]
	
def get_page2():
	print("Downloading the page to find the image2...")
	web_content=urllib2.urlopen('http://www.aapodx2.com/').read()
	patron = re.compile('.*href=\"(.*?)\"><img')
	matcher = patron.findall(web_content)
	return 'http://www.aapodx2.com'+matcher[1]
	
def get_img_ext(url):
	patron = re.compile('\.jpg|\.png')
	matcher = patron.findall(url)
	return matcher[0]
	
def download_img(url,loc_dir):
	img_ext = get_img_ext(url)
	loc = loc_dir+'/'+today+'-apod'+img_ext
	print("Downloading the image '"+url+"' in '"+loc+"'...")
	urllib.urlretrieve(url,loc)

# ~ url1=get_page1()
# ~ print(url1)

# ~ url2=get_page2()
# ~ print(url2)

# ~ download_img(url1,'apod1')
# ~ download_img(url2,'apod2')
# ~ download_img('www.google.com/aaa.jpg','trash')

try:
    # ~ resp = urllib2.urlopen("http://www.google.com/this-gives-a-404/")
    resp = urllib2.urlopen("http://www.aapodx2.com/2018/20181209.jpg")
except urllib2.URLError, e:
    if not hasattr(e, "code"):
        raise
    resp = e

print "Gave", resp.code, resp.msg
print "=" * 80
print resp.read(80)
