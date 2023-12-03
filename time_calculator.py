def add_time(start, duration, weekStartDay=''):
   
    # Split the start time into hours and minutes and convert them into Integer
    start_time = start.split()
    start_hours = int(start_time[0].split(":")[0])
    start_minutes = int(start_time[0].split(":")[1])

    # Split the duration into hours and minutes and convert them into Integer
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    #convert to 24 hour time
    start_hours_24 = start_hours + 12 if start_time[1] == 'PM' else start_hours
    
    totalHour = start_hours_24 + duration_hour
    thisMinute = start_minutes + duration_minutes
    if thisMinute > 59:
        thisMinute -= 60
        totalHour += 1

    thisDaylight = 'AM' if totalHour % 24 < 12 else 'PM'
    thisHour = totalHour % 12 if totalHour % 12 != 0 else 12
    minuteStr = ('0'+str(thisMinute)) if thisMinute < 10 else str(thisMinute)
  
    if (totalHour <24):
        dayGap = ''
    elif (totalHour <48):
        dayGap = ' (next day)'
    else:
        dayGap = ' (' + str(totalHour//24) + ' days later)'

    if weekStartDay != '':
        return str(thisHour) + ':' + minuteStr + ' '+ thisDaylight + ', '+newDay(totalHour//24,standardizeDay(weekStartDay)) + dayGap
    else:
        return str(thisHour) + ':' + minuteStr + ' ' + thisDaylight + dayGap


def newDay(x,weekStartDay):
    dayList = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return dayList[(dayList.index(weekStartDay) + x) % 7]

def standardizeDay(x):
    return(x.lower().capitalize())

