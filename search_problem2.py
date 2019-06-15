#!/usr/bin/python3


from  googlesearch import search
import webbrowser
import time
list_=[]
ser=input("enter the name you want to search : ")
for  i in search(ser,stop=10):
	print(i)
	time.sleep(1)
	list_.append(i)
	file_=open("url.txt","a+")
	file_.write("\n")
	file_.write(i)
file_.close()
print(list_)


