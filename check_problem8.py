#!/usr/bin/python3
import os
import pyttsx3 
cmd=input("enter command:")
r=os.system(" {} 2>/dev/null".format(cmd))
file_=open("command.txt","a+")
file_.write(cmd)
file_.write("\n")
if r == 0:
	print("right command")
else:
	print("wrong command")

yes=0
with open("command.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if cmd in part:
                yes=1

if yes == 1:
	sound_driver=pyttsx3.init()
	sound_driver.say("don't do this again")
	sound_driver.runAndWait()
