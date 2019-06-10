import datetime
name=input("Enter Your Name :")
age=int(input("Enter your age :"))
age_95 = datetime.datetime.now()
print(name," Will turn 95 year old in ",(95-age)+age_95.year)
