def parse_listings_into_sms(stringhtml):
	sms = ("Hier die Top 3 Partys in London heute:\n")

	leftboundEvents = stringhtml.find('<li><p class="eventDate date">')

	rightbound_i_name = 0

	for i in range(0,3): 
		"""i is the place in top 3"""

		leftbound_i_name = stringhtml.find('Event details of ', leftboundEvents + rightbound_i_name) + len('Event details of ')
		rightbound_i_name = stringhtml.find('"', leftbound_i_name)

		leftbound_i_club = stringhtml.find('href', rightbound_i_name)
		leftbound_i_club = stringhtml.find('>', leftbound_i_club) + 1
		rightbound_i_club = stringhtml.find('<', leftbound_i_club)

		i_name = stringhtml[leftbound_i_name:rightbound_i_name]
		i_club = stringhtml[leftbound_i_club:rightbound_i_club]

		self.__sms = self.__sms + str(i+1) + ": " + i_name + " @ " + i_club + "\n"
	
	return sms
