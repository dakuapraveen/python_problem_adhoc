import datetime
name=input("Enter your name:")
current_time=datetime.datetime.now()
if 0 <= current_time.hour < 12:
	print("good morning",name)
elif 12 <= current_time.hour < 17:
	print("goodafter noon",name)
elif 17 <= current_time.hour < 20:
	print("good evening",name)
elif 20 <= current_time.hour <= 23:
	print("good night",name)