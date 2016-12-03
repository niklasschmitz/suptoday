class Event(object):
	def __init__(self, pos, name='', club=''):
		super(Event, self).__init__()
		self.__pos = int(pos) 
		"""position in the top 5"""
		self.__name = str(name)
		self.__club = str(club)
		self.__sms = ""

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name	

	def getClub(self):
		return self.__club

	def setClub(self, club):
		self.__club = club



class ContentRipper(object):
	def __init__(self):
		self.__Events = [Event(1), Event(2), Event(3)]

	def readoutListing_HTML_String(self, stringhtml):
		self.__sms = ("Hier die Top 3 Partys in Berlin heute:\n")

		leftboundEvents = stringhtml.find('<li><p class="eventDate date">')

		rightbound_i_name = 0

		for i in range(0,3): 
			"""i is the place in top 5"""

			leftbound_i_name = stringhtml.find('Event details of ', leftboundEvents + rightbound_i_name) + len('Event details of ')
			rightbound_i_name = stringhtml.find('"', leftbound_i_name)

			leftbound_i_club = stringhtml.find('href', rightbound_i_name)
			leftbound_i_club = stringhtml.find('>', leftbound_i_club) + 1
			rightbound_i_club = stringhtml.find('<', leftbound_i_club)
			
			i_name = stringhtml[leftbound_i_name:rightbound_i_name]
			i_club = stringhtml[leftbound_i_club:rightbound_i_club]

			self.__Events[i].setName(i_name)
			self.__Events[i].setClub(i_club)


			self.__sms = self.__sms + str(i+1) + ": " + self.__Events[i].getName() + " @ " + self.__Events[i].getClub() + "\n"

			
	def getSMS(self):
		return self.__sms

def main(stringhtml=""" """):
        c = ContentRipper()
        c.readoutListing_HTML_String(stringhtml)
        return c.getSMS()
        
			

		












