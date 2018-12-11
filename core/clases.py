#core.clases
#by boot1110001

### IMPORTS ####################################################################
import re #for regex
from urllib import urlopen #to download websites

### CLASES #####################################################################
class BgImg:
	def __init__(self, distinct, url, loc_dir, now):
		patron = re.compile('\.(jpg|jpeg|png|gif)$')
		matcher = patron.findall(url)

		remote_file = urlopen(url)
		meta = remote_file.info()

		self.url = url
		self.distinct = distinct
		self.dir = loc_dir
		self.exdate = now
		self.ext = matcher[0]
		self.fsize = meta.getheaders("Content-Length")[0]
		self.fname = now+'-'+distinct+'.'+matcher[0]

	def get_loc(self):
		return self.dir+'/'+self.fname

	def get_date(self):
		fname_list=self.fname.split('-')
		return fname_list[0]+'-'+fname_list[1]+'-'+fname_list[2]

	def to_string(self):
		string="="*80+"\n"
		string+="My file name is: "+self.fname+"\n"
		string+="My URL is: "+self.url+"\n"
		string+="My localization is: "+self.get_loc()+"\n"
		string+="My directory is: "+self.dir+"\n"
		string+="My execution date is: "+self.exdate+"\n"
		string+="My date is: "+self.get_date()+"\n"
		string+="My distinct is: "+self.distinct+"\n"
		string+="My extension is: "+self.ext+"\n"
		string+="My size in bytes is: "+self.fsize+"\n"
		string+="="*80+""
		return string

	def __eq__(self,other):
		out=False
		if (other.dir and other.distinct and other.ext and other.fsize and other.get_date()):
			if (other.dir==self.dir and other.distinct==self.distinct and other.ext==self.ext and other.fsize==self.fsize and other.get_date() == self.get_date()):
				out=True
		return out

	def __ne__(self, other):
		#Overrides the default implementation (unnecessary in Python 3)
		return not self.__eq__(other)

class LocalBgImg:
	def __init__(self, fname, loc_dir):
		patron = re.compile('\.(jpg|jpeg|png|gif)$')
		matcher = patron.findall(fname)
		fname_list=fname.split('-')

		local_file = open(loc_dir+'/'+fname, "rb")
		self.fsize=str(len(local_file.read()))
		local_file.close()

		self.dir = loc_dir
		self.fname = fname
		self.ext = matcher[0]
		self.exdate = fname.replace('-'+fname_list[-1],'')
		self.distinct = fname_list[-1].replace('.'+matcher[0],'')

	def get_loc(self):
		return self.dir+'/'+self.fname

	def get_date(self):
		fname_list=self.fname.split('-')
		return fname_list[0]+'-'+fname_list[1]+'-'+fname_list[2]

	def to_string(self):
		string="="*80+"\n"
		string+="My file name is: "+self.fname+"\n"
		string+="My localization is: "+self.get_loc()+"\n"
		string+="My directory is: "+self.dir+"\n"
		string+="My execution date is: "+self.exdate+"\n"
		string+="My date is: "+self.get_date()+"\n"
		string+="My distinct is: "+self.distinct+"\n"
		string+="My extension is: "+self.ext+"\n"
		string+="My size in bytes is: "+self.fsize+"\n"
		string+="="*80+""
		return string

	def __eq__(self,other):
		out=False
		if (other.dir and other.distinct and other.ext and other.fsize and other.get_date()):
			if (other.dir==self.dir and other.distinct==self.distinct and other.ext==self.ext and other.fsize==self.fsize and other.get_date() == self.get_date()):
				out=True
		return out

	def __ne__(self, other):
		#Overrides the default implementation (unnecessary in Python 3)
		return not self.__eq__(other)
