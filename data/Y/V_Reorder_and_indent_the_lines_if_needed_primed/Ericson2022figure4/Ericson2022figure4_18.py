def alarm_clock(day, vacation):
    if day == 0 or day == 6:
        if vacation:
            return '10:00'
        return 'off'
    else:
        if vacation:
            return '7:00'
        return '10:00'
