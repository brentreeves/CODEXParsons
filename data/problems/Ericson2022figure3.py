# Put the code in order to define a Person class with a constructor (__init__), a method to print the object attributes (__str__), and an initials method which returns the first letter of the first name and the first letter of the last name.
class Person:
Class Person:
	def __init__(self, first, last):
	def __init__(first, last):
		self.first = first
		self.last = last
	def __str__(self):
		return (self.first + " " + self.last)
		return (self.first + self.last)
	def initials(self):
		return(self.first[0] + self.last[0])
		return(self.first[1] + self.last[1])
