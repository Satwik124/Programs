import pytz ,datetime
Year=int(input())
Month=int(input())
Day=int(input())
Hour=int(input())
Minute=int(input())
#converting into date time
users_time=datetime.datetime(Year,Month,Day,Hour,Minute)
#converting into timezones
cairo_timezone=pytz.timezone('Africa/cairo')
London_timezone=pytz.timezone("UTC")
NewDelhi_timezone=pytz.timezone('Asia/Kolkata')
Sydney_timezone=pytz.timezone('Australia/Sydney')
Tokyo_timezone=pytz.timezone('Asia/Tokyo')
Seoul_timezone=pytz.timezone('Asia/Seoul')

cairo_time=pytz.utc.localize(users_time).astimezone(cairo_timezone)
London_time=pytz.utc.localize(users_time).astimezone(London_timezone)
NewDelhi_time=pytz.utc.localize(users_time).astimezone(NewDelhi_timezone)
Sydney_time=pytz.utc.localize(users_time).astimezone(Sydney_timezone)
Tokyo_time=pytz.utc.localize(users_time).astimezone(Tokyo_timezone)
Seoul_time=pytz.utc.localize(users_time).astimezone(Seoul_timezone)

print("Cairo Time is",cairo_time.isoformat())
print("London Time is",London_time.isoformat())
print("New Delhi Time is",NewDelhi_time.isoformat())
print("Sydney Time is",Sydney_time.isoformat())
print("Tokyo Time is",Tokyo_time.isoformat())
print("Seoul Time is",Seoul_time.isoformat())
