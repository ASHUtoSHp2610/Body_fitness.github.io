# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:37:36 2021

@author: sheet
"""

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

#root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Body Fitness")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('BFc.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Body Fitness", font=('times', 40,' bold '), height=1, width=60,bg="Black",fg="white")
lbl.place(x=0, y=2)


framed = tk.LabelFrame(root, text="--WELCOME--", width=500, height=250, bd=15, font=('times', 20, ' bold '),bg="AliceBlue")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=700, y=350)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login',bg='black',fg='white',command=login,width=10,font=('times', 20,' bold ')).place(x=40,y=55)
button1 = tk.Button(framed, text='Register',bg='black',width=10,fg='white',command=reg,font=('times', 20,' bold ')).place(x=255,y=55)


root.mainloop()
