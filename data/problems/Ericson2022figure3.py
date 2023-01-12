# Put the code in order to define a Person class with a constructor (__init__), a method to print the object attributes (__str__), and an initials method which returns the first letter of the first name and the first letter of the last name.
class Person:
	def_init_(self, first, last):
		self.first = first
		self.last = last
	def_str_(self):
		return (self.first + " " + self.last)
	def initials(self):
		return(self.first[0] + self.last[0])
