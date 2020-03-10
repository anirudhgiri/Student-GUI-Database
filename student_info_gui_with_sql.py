#Author : Anirudh Giri
#Date   : 10th March, 2020

import tkinter as tk #importing the tkinter module for GUI operations
import sqlite3 #importing the sqlite 3 modile for database operations

#---Database Section---
conn = sqlite3.connect("Students.db") #creating a conncection to the Students.db file
crsr = conn.cursor() #creating a cursor for the db file

query = "create table if not exists Students(rNo varchar(50), name varchar(50), dept varchar(50), gender varchar(6), age int)"
crsr.execute(query) #creating the table "Students"

def insert(): #functon for INSERT operation
    query = 'insert into Students values("{rNo}", "{name}", "{dept}", "{gender}", {age})'.format(rNo=regVal.get(), name=nameVal.get(), dept=deptVal.get(), gender=genderVal.get(), age=int(ageVal.get()))
    crsr.execute(query) #inserting the given values into the Students table

def show():#function for SELECT operation
    query = 'select * from Students'
    crsr.execute(query) #selecting all values from the Students table for display
    for val in crsr.fetchall():
        print("{rNo} {name} {dept} {gender} {age}".format(rNo=val[0], name=val[1], dept=val[2], gender=val[3], age=val[4]))

#---GUI Section---
window = tk.Tk() #creating a window

#Registration Number Input as Text Entry
regLabel = tk.Label(text = "RegNo").grid(row=0, column=0)
regVal = tk.StringVar()
regEntry = tk.Entry(textvariable = regVal).grid(row=0, column=1)

#Name Input as Text Entry
nameLabel = tk.Label(text = "Name").grid(row=1, column=0)
nameVal = tk.StringVar()
nameEntry = tk.Entry(textvariable = nameVal).grid(row=1, column=1)

#Department Input as Text Entry
deptLabel = tk.Label(text = "Dept").grid(row=2, column=0)
deptVal = tk.StringVar()
deptEntry = tk.Entry(textvariable = deptVal).grid(row=2, column=1)

#Gender Input as Radiobuttons
genderLabel = tk.Label(text = "Gender").grid(row=3, column=0)
genderVal = tk.StringVar(value = "Male")
maleRadioButton = tk.Radiobutton(text="Male", variable = genderVal, value="Male").grid(row=3, column=1)
femaleRadioButton = tk.Radiobutton(text="Female", variable = genderVal, value="Female").grid(row=3, column=2)

#Age Input as Spinbox
ageLabel = tk.Label(text = "Age").grid(row=4, column=0)
ageVal = tk.StringVar()
ageSpinBox = tk.Spinbox(from_ = 18, to=100, textvariable = ageVal).grid(row=4, column=1)

#Button for Insertion into Students table
inButton =  tk.Button(text = "Insert", command=insert).grid(row=5, column=0)

#Button for Selection from Students table
shButton =  tk.Button(text = "Show", command=show).grid(row=5, column=1)

#Run the mainloop of the window
window.mainloop()