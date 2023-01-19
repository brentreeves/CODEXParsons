def alarm_clock(day, vacation):
if vacation:
return 'off'
elif day == 0 or day == 6:
return '10:00'
else:
return '7:00'
