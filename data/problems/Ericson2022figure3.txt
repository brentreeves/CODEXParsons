class Person:
	def_init_(self, first, last):
		self.first = first
		self.last = last
	def_str_(self):
		return (self.first + " " + self.last)
	def initials(self):
		return(self.first[0] + self.last[0])