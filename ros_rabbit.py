#!/usr/bin/env python
#from std_msgs.msg import Float32
#import rospy

from Tkinter import *
from datetime import timedelta

PATH = ""
goal = 480 # 8 min
t = 0
BD = 1 # Boxes Delivered
LDT = 1 # Linear Distance Traveled
Score = (5*BD)+(LDT*0.10)

def avg_time():
	return t/BD

def countdown():
	global t
	at = avg_time()
	td = timedelta(seconds = t)
	if t >= goal:
		r1_1.config(foreground = "red")
		r2_1.config(foreground = "red")
		r5_1.config(foreground = "red")
	
	if at > goal/18:
		r6_2.config(foreground = "red")

	r1_1.config(text = td)
	r2_1.config(text = t)
	r4_1.config(text = BD)
	r4_2.config(text = LDT)
	r4_3.config(text = Score)
	r6_2.config(text = avg_time())
	t += 1
	r1_1.after(1000,countdown)


def stop():
	with open("{}log.csv".format(PATH), mode = "w") as f:
		f.write("Time Taken,Boxes Delivered,Linear Distance Traveled,Average Time,Score\n{},{},{},{},{}".format(t,BD,LDT,avg_time(),Score))
	exit()

#Canvas
win = Tk()
win.title("ROS Rabbit")
win.config(bg = "black")

#Labels
r1_1 = Label(win,text = "0:00:00",font = "arial 30", foreground = 'green', background = "black")
r1_2 = Label(win,text ="|", font = "arial 30", foreground = 'yellow',background = "black")
r1_3 = Label(win,text = timedelta(seconds = goal), font = "arial 30", foreground = 'green',background = "black")

r2_1 = Label(win,text = "0.0",font = "arial 30", foreground = 'green', background ="black")
r2_2 = Label(win,text ="|", font = "arial 30", foreground = 'yellow',background = "black")
r2_3 = Label(win,text = str(goal), font = "arial 30", foreground = 'green',background ="black")

r3_1 = Label(win,text = "BD", font = "arial 30", foreground = 'royal blue',background ="black")
r3_2 = Label(win,text = "LDT", font = "arial 30", foreground = 'royal blue',background ="black")
r3_3 = Label(win,text = "Score", font = "arial 30", foreground = 'royal blue',background ="black")

r4_1 = Label(win,text = "0.0", font = "arial 30", foreground = 'yellow',background ="black")
r4_2 = Label(win,text = "0.0", font = "arial 30", foreground = 'yellow',background ="black")
r4_3 = Label(win,text = "0.0", font = "arial 30", foreground = 'yellow',background ="black")

r5_1 = Label(win,text = "Time Limit Exceeded!", font = "arial 15", foreground = 'black', background ="black")

r6_1 = Label(win,text = "Avg Time", font = "arial 30", foreground = 'royal blue', background ="black")
r6_2 = Label(win,text = "0.0", font = "arial 30", foreground = 'yellow', background ="black")

#Button
b1 = Button(win,text="Stop", command = stop, activebackground = "green", background = "gray24", foreground = "green")

#Positioning
r1_1.grid(row = 1,column = 1)
r1_2.grid(row = 1,column = 2)
r1_3.grid(row = 1, column = 3, padx = 3)

r2_1.grid(row = 2,column = 1)
r2_2.grid(row = 2,column = 2)
r2_3.grid(row = 2, column = 3)

r3_1.grid(row = 3,column = 1)
r3_2.grid(row = 3,column = 2)
r3_3.grid(row = 3, column = 3)

r4_1.grid(row = 4,column = 1)
r4_2.grid(row = 4,column = 2)
r4_3.grid(row = 4, column = 3)

r5_1.grid(row = 5, column = 2)

r6_1.grid(row = 6, column = 1, padx = 3)
r6_2.grid(row = 6, column = 2)
b1.grid(row = 6, column = 3, padx = 2, pady = 5)

countdown()
mainloop()