#!/usr/bin/python3
print("different functions of cat command")
print("""1) for show the content of file :
2) for cat file1 > file2 :
3) for cat file1 >> file2 :
4) for display $ at the end of every line {cat -E}: """)
ch=int(input("enter your choice"))
if ch == 1:
	first=input("enter file name")
	con=open(first,"r")
	print(con.read())
	con.close()

if ch == 2:
	first=input("enter source file name")
	con=open(first,"r")
	second=input("enter second file name")
	con1=open(second,"w")
	con1.write(con.read())
	con.close()
	con1.close()

if ch == 3:
	first=input("enter source file name")	
	con=open(first,"r")
	second=input("enter second file name")
	con1=open(second,"a+")
	con1.write(con.read())
	con.close()
	con1.close()
if ch == 4:
	first=input("enter file name")
	con=open("try1.txt","r")
	line=con.readline()
	while line:
		print(line+"$")
		line=con.readline()
	con.close()
