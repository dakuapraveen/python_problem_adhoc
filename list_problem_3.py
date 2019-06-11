adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
grat_five=[]
less_eql_two=[]
for i in adhoc:
	if int(i) > 5:
		grat_five.append(i)
	elif int(i) <= 2:
		less_eql_two.append(i)
print(grat_five)
print(less_eql_two)
