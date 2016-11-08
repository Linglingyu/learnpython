from datetime import datetime

now = datetime.now()
# print(now)

# dt=datetime(2015,4,19,12,20)
# print(dt)

# print(dt.timestamp())

# t=1234567800.0
# print(datetime.fromtimestamp(t))#本地时间
# print(datetime.utcfromtimestamp(t))#UTC时间

#str转换为datetime
cday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)

#datatime转换为str
print(now.strftime('%a,%b %d %H:%M'))


from datetime import timedelta
print(now+timedelta(hours=10))
print(now+timedelta(days=2,hours=10))


