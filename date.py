import time
from datetime import datetime
now = datetime.now()
print("a)Current date and time:",now)
print("b)Current year:",now.year)
print("c)Moth of the year:",now.strftime("%B"))
print("d)Week number of the year:",now.strftime("%U"))
print("e)Weekday of the week:",now.strftime("%A"))
print("f)Day of year:",now.strftime("%j"))
print("g)Day of month:",now.day)
print("h)Day of week:",time.strftime("%W"))
