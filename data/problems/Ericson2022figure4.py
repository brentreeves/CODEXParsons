# Put the code blocks below in order to solve the following problem. There are two extra blocks that are not needed in a correct solution. Given a day of the week encoded as 0=Sum, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekends it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
def alarm_clock(day, vacation)
	if vacation:
		if day == 0 or day == 6:
		if day == 0 || day == 6:
			return 'off'
		else:
			return '10:00'
	else:
		if day == 0 or day == 6:
			return '10:00'
		else:
			return '7:00'
