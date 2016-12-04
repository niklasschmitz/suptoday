class Event(object):
	def __init__(self, pos, name='', club=''):
		super(Event, self).__init__()

		self.__pos = int(pos) 			#pos in the RA listing
		self.__name = str(name)
		self.__club = str(club)

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name	

	def getClub(self):
		return self.__club

	def setClub(self, club):
		self.__club = club

