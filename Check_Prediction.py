# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:31:48 2023

@author: CAPTAIN

"""




from tkinter import *
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  
from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk, ImageFilter
from tkinter import ttk
import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from subprocess import call
from joblib import dump , load
from PIL import ImageTk, Image
import tempfile
import sqlite3


root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# root.geometry("1700x1500+250+5")
root.title("Body Fitness Prediction")
root.configure(background="white")
label = tk.Label(root, text="Diet Plan")
image = Image.open("BF4.jpg")
#image = image.filter(ImageFilter.BLUR)
image = image.resize((2000, 1000), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# Create a label widget and set the image as the background
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0) 
label.pack()



def Train():
    #GUI
    '''

    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
   # root.geometry("1700x1500+250+5")
    root.title("Body Fitness Prediction")
    root.configure(background="white")
    label = tk.Label(root, text="Diet Plan")
    image = Image.open("BF4.jpg")
    #image = image.filter(ImageFilter.BLUR)
    image = image.resize((2000, 1000), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image)

    # Create a label widget and set the image as the background
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0) 
    label.pack()
'''
    
    #root.configure(background=img)
    
    age = tk.IntVar()
    gender = tk.StringVar()
    height_cm = tk.IntVar()
    weight_kg = tk.IntVar()
    body_fat = tk.IntVar()
    diastolic = tk.IntVar()
    systolic =  tk.IntVar()
    gripForce = tk.IntVar()
    sit_and_bend_forward_cm = tk.IntVar()
    sit_ups_counts = tk.IntVar()
    broad_jump_cm = tk.IntVar()
    
    
    
    #===================================================================================================================


    lbl = tk.Label(root, text="Predictor", font=('times', 40,' bold '), height=1, width=60,bg="black",fg="white",bd=5, relief="solid")
    lbl.place(x=0, y=2)
    def Detect():
        e1=age.get()
        print(e1)
        
        e2=gender.get()
        if e2=="F":
            e2=0
        else :
            e2=1
        print(e2)
        
        e3=height_cm.get()
        print(e3)
        
        e4=weight_kg.get()
        print(e4)
        
        e5=body_fat.get()
        print(e5)
        
        e6=diastolic.get()
        print(e6)
        
        e7=systolic.get()
        print(e7)
        
        e8=gripForce .get()
        print(e8)
        
        e9=sit_and_bend_forward_cm.get()
        print(e9)
        
        e10=sit_ups_counts.get()
        print(e10)
        
        e11=broad_jump_cm.get()
        print(e11)
        
        
        with open("example.txt", "w") as f:
            f.write(f"{e1}, {e2}, {e3}, {e4}, {e5}, {e6}, {e7}, {e8}, {e9}, {e10}, {e11}")
            
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('DT.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
        print(v)
        
    
        if v[0]==0:
           print("Low Body Fitness")
           yes = tk.Label(root,text="Low Body Fitness",background="lavender",foreground="black",font=('times', 20, ' bold '),width=50,bd=4, relief="solid")
           yes.place(x=540,y=850)
           
           
           
        if v[0]==1:
           print("Medium Body Fitness")
           yes = tk.Label(root,text="Medium Body Fitness",background="lavender",foreground="black",font=('times', 20, ' bold '),width=50,bd=4, relief="solid")
           yes.place(x=540,y=850)
           
        if v[0]==2:
            print(" Good Body Fitness")
            yes = tk.Label(root,text="Good Body Fitness",background="lavender",foreground="black",font=('times', 20, ' bold '),width=50,bd=4, relief="solid")
            yes.place(x=540,y=850)
            certi_button = tk.Button(root, foreground="white", background="black",text="Certificate",command=Certificate,font=('times', 20, ' bold '),width=10,bd=4, borderwidth=7, relief="sunken")
            certi_button.place(x=830,y=900)
            


           
      

    l1=tk.Label(root,text="Age",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l1.place(x=700,y=100)
    age = tk.Entry(root, width=5, font=("TkDefaultFont", 20), textvariable=age, bd=4, relief="solid")
    age.place(x=1095,y=100)

    l2=tk.Label(root,text="Gender",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l2.place(x=700,y=160)
    monthchoosen = ttk.Combobox(root, width = 7, textvariable = gender)
       
    monthchoosen['values'] = ('Female','Male')
    monthchoosen.place(x=1095,y=160)
      
    monthchoosen.current()

    l3=tk.Label(root,text="Height",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l3.place(x=700,y=220)
    height_cm=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=height_cm, relief="solid")
    height_cm.place(x=1095,y=220)
    
    
    l4=tk.Label(root,text="Weight",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l4.place(x=700,y=280)
    weight_kg=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=weight_kg, relief="solid")
    weight_kg.place(x=1095,y=280)

    l5=tk.Label(root,text="Body Fat",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l5.place(x=700,y=340)
    body_fat=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=body_fat, relief="solid")
    body_fat.place(x=1095,y=340)

    l6=tk.Label(root,text="Diastolic",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l6.place(x=700,y=400)
    diastolic=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=diastolic, relief="solid")
    diastolic.place(x=1095,y=400)
    
    
    l7=tk.Label(root,text="Systolic",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l7.place(x=700,y=460)
    systolic=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=systolic, relief="solid")
    systolic.place(x=1095,y=460)
    
    
   

    l8=tk.Label(root,text="Grip Force",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l8.place(x=700,y=520)
    gripForce=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=gripForce, relief="solid")
    gripForce.place(x=1095,y=520)

    l9=tk.Label(root,text="Sit & Bend Forward",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l9.place(x=700,y=580)
    sit_and_bend_forward_cm=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=sit_and_bend_forward_cm, relief="solid")
    sit_and_bend_forward_cm.place(x=1095,y=580)
    
    l9=tk.Label(root,text="Sit Ups Counts",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l9.place(x=700,y=640)
    sit_ups_counts=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=sit_ups_counts, relief="solid")
    sit_ups_counts.place(x=1095,y=640)
    
    
    l9=tk.Label(root,text="Broad Jump",background="cornsilk",font=('times', 20, ' bold '),width=20,bd=4, relief="solid")
    l9.place(x=700,y=700)
    broad_jump_cm=tk.Entry(root,bd=4,width=5,font=("TkDefaultFont", 20),textvar=broad_jump_cm, relief="solid")
    broad_jump_cm.place(x=1095,y=700) 
    
    
    def diet():
        print('Diet')
        call(['python', 'diet.py'])
    
    def Certificate():
        print('Certificate')
        call(['python', 'certificate.py'])
        
    def Exercise():
        print("Exercise")
        call(['python', 'exercise.py'])
    
    
    
    button1 = tk.Button(root, foreground="white", background="black",text="Submit",command=Detect,font=('times', 20, ' bold '),width=10,bd=4,borderwidth=7, relief="sunken")
    button1.place(x=650,y=750)
    
    button2 = tk.Button(root, foreground="white", background="black",text="Diet Plan",font=('times', 20, ' bold '),width=10, command = diet,bd=4, borderwidth=7,relief="sunken")
    button2.place(x=850,y=750)
    
    button3 = tk.Button(root, foreground="white", background="black",text="Exericse",font=('times', 20, ' bold '),width=10, command = Exercise,bd=4,borderwidth=7, relief="sunken")
    button3.place(x=1050,y=750)
    
    def home():
        print('Home')
        call(['python','GUI_Master.py'])
            
    image1 = Image.open("home_button.png")
    image1 = image1.resize((105, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    
    button4 = tk.Button(root, image=photo,font=('times', 2, ' bold '), command=home,background="black", bd=5, relief="solid")
    button4.place(x=1810, y=2)
    


    root.mainloop()

Train()