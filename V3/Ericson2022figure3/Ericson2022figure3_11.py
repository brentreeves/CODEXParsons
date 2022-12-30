class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def initials(self):
        return(self.first[0] + self.last[0])
    def __str__(self):
        return (self.first + " " + self.last)
