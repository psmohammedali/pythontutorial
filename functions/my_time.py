import time
import calendar
import datetime
#print(time.localtime)
# print(calendar.iterweekdays)

#print(calendar.calendar(1999))


#print(calendar.month(1999,10))

# obj =  calendar.Calendar.itermonthdays(2000,4,5)
# print(obj)

# print(datetime.datetime.now.())

import datetime

now = datetime.datetime.now()

# current_time = datetime.datetime.now().strftime("%H:%M:%S")
# print(type(current_time))
#

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
date = int(input("Enter the Day: "))

# print(calendar.isleap(year))
day_name = datetime.date(year, month, date)
print(day_name.day)
print(day_name.strftime("%c"))