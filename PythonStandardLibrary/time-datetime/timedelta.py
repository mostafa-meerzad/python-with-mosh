import datetime


now = datetime.datetime.now()
diff = now - datetime.timedelta(days=1)
future = now + datetime.timedelta(
    days=100, hours=1, minutes=1, seconds=100, weeks=100, microseconds=10000000
)
print(f"now: {now}, a day ago: {diff}, future: {future}")
