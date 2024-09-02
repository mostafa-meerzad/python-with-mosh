import datetime
import time

now = datetime.datetime.now()
print(now)


# print(datetime.today())

myDate = datetime.datetime(2019, 1, 1) # create a datetime object with specific values
print(myDate)
myTime = datetime.datetime.strptime("2018 4 8", "%Y %m %d") # parse datetime from a string
# Note: the datetime string and the format provided must match, the delimiter and position of values and number of characters
print(myTime)

myDateTime = datetime.datetime.fromtimestamp(time.time()) # convert a timestamp into datetime object
print(myDateTime)

strTime = datetime.datetime.now().strftime( "%h:%m:s") # format time object into string
print(strTime)

print(datetime.date(1919, 1, 1))
print(datetime.time(12, 3, 1))

print()
print(f"year: {myDate.year}, month: {myDate.month}, day: {myDate.day}, hour: {myDate.hour}") # datetime object has these properties