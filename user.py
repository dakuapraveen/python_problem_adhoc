#!/usr/bin/python3
import os
import crypt
uname=input("Enter username : ")
flag=0
for i in uname:
	if i.isalpha() != True: #check whether user name is char or not
		flag=1
	else :
		continue
if flag == 0:
	passwd="hello"+uname
	use_pass=crypt.crypt(passwd,"ck")
	os.system("sudo useradd -m -p"+use_pass+" "+uname)
	print("user created!!")
else:
	print("All characters are not string!!")
	
