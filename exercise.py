# -*- coding: utf-8 -*-
"""
Created on Tue May 16 00:04:19 2023

@author: CAPTAIN
"""

import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from subprocess import call
from joblib import dump , load
from PIL import ImageTk, Image



def train():
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    #root.geometry("3000x1000")
    root.title("Body Fitness Prediction")
    root.configure(background="white")
    label = tk.Label(root, text="Diet Plan")
    image = Image.open("bg1.jpg")
    image1 = Image.open("home_button.png")
    image1 = image1.resize((105, 60), Image.ANTIALIAS)
    image = image.resize((3000, 1000), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(image)

    # Create a label widget and set the image as the background
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0) 
    label.pack()
    
    with open("example.txt", "r") as f:
        input_data = f.read()
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11= map(int, input_data.strip().split(','))
    
    
    
    from joblib import dump , load
    a1=load('DT.joblib')
    v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
    print(v)
    lbl = tk.Label(root, text="Exercise Plan", font=('times', 40,' bold '), height=1, width=60,bg="black",fg="white",bd=4, relief="solid")
    lbl.place(x=0, y=2)
    
    def chest():
        if v[0]==0:
            lf1 = tk.Label(root,text="Chest Workout:\n1.push-up\n2.Barbell Bench Press\n3.Dips\n4.Incline Push Up\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            lf1.place(x=800,y=400)
            
        
        if v[0]==1:
            mf1 = tk.Label(root,text="Chest Workout:\n1.push-up\n2.Barbell Bench Press\n3.Dips\n4.Incline Push Up\n5.Burpee\n6.Barbell Bench Press\n7.Barbell Incline Bench Press\n8.Chest Stretch\n\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf1.place(x=800,y=400)
        
        if v[0]==2:
            mf1 = tk.Label(root,text="Chest Workout:\n1.push-up\n2.Barbell Bench Press\n3.Dips\n4.Incline Push Up\n5.Burpee\nBarbell Bench Press\n6.Barbell Incline Bench Press\n7.Chest Stretch\n8.Barbell Floor Press\n9.Barbell Larsen Bench Press\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf1.place(x=800,y=400)
            
            
    def backWorkout():
        if v[0]==0:
            lf2 = tk.Label(root,text="Back Workout:\n1.Pull Ups\n2.Machine Pulldown\n3.Dumbbell Row Unilateral\n4.Lats Stretch Variation One\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")            
            lf2.place(x=800,y=400)
        
        if v[0]==1:
            mf2 = tk.Label(root,text="Back Workout:\n1.Pull Ups\n2.Machine Pulldown\n3.Dumbbell Row Unilateral\n4.Lats Stretch Variation One\n5.Barbell Bent Over Row\n6.Barbell Landmine Row\n7.Barbell Meadows Row\n\n\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf2.place(x=800,y=400)
        
        if v[0]==2:
            mf2 = tk.Label(root,text="Back Workout:\n1.Pull Ups\n2.Machine Pulldown\n3.Dumbbell Row Unilateral\n4.Lats Stretch Variation One\n5.Barbell Bent Over Row\n6.Barbell Landmine Row\n7.Barbell Meadows Row\n8.Barbell Deadlift\n9.Elevated Pike Press\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf2.place(x=800,y=400)
        
    def Arm():
        if v[0]==0:
            lf3 = tk.Label(root,text="Arm Workout:\n1.Barbell Curl\n2.Dumbbell Curl\n3.Dumbbell Hammer Curl\n4.Dumbbell Incline Hammer Curl\n5.Bench Dips",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            lf3.place(x=800,y=400)
        
        if v[0]==1:
            mf3 = tk.Label(root,text="Arm Workout:\n1.Barbell Curl\n2.Dumbbell Curl\n3.Dumbbell Hammer Curl\n4.Dumbbell Incline Hammer Curl\n5.Bench Dips\n6.Diamond Push Ups\n7.Barbell Reverse Curl\n8.Cable Bayesian Curl\n9.Cable Twisting Curl\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf3.place(x=800,y=400)
        
        if v[0]==2:
            mf3 = tk.Label(root,text="Arm Workout:\n1.Barbell Curl\n2.Dumbbell Curl\n3.Dumbbell Hammer Curl\n4.Dumbbell Incline Hammer Curl\n5.Bench Dips\n6.Diamond Push Ups\n7.Barbell Reverse Curl\n8.Cable Bayesian Curl\n9.Cable Twisting Curl\n10.Barbell Reverse Curl",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf3.place(x=800,y=400)
        
    def Shoulders():
        if v[0]==0:
            lf4 = tk.Label(root,text="Shoulders Workout: \n1.Dumbbell Lateral Raise\n2.Dumbbell Front Raise\n3.Shoulders Stretch\n4.Cable Overhead Press\n5.Dumbbell Laying Reverse Fly",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            lf4.place(x=800,y=400)
        
        if v[0]==1:
            mf4 = tk.Label(root,text="Shoulders Workout: \n1.Dumbbell Lateral Raise\n2.Dumbbell Front Raise\n3.Shoulders Stretch\n4.Cable Overhead Press\n5.Dumbbell Laying Reverse Fly\n6.Cable Rear Delt Fly\n7.Barbell Overhead Press\n8.Barbell Front Raise\n\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf4.place(x=800,y=400)
        
        if v[0]==2:
            mf4 = tk.Label(root,text="Shoulders Workout: \n1.Dumbbell Lateral Raise\n2.Dumbbell Front Raise\n3.Shoulders Stretch\n4.Cable Overhead Press\n5.Dumbbell Laying Reverse Fly\n6.Cable Rear Delt Fly\n7.Barbell Overhead Press\n8.Barbell Front Raise\n9.Barbell Upright Row\n10.Barbell Z Press",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf4.place(x=800,y=400)
        
    def legs():
        if v[0]==0:
            lf5 = tk.Label(root,text="Leg Workout:\n1.Quads Stretch\n2.Calves Stretch\n3.Calves Stretch\n4.Hamstrings Stretch\n5.Bodyweight Squat",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            lf5.place(x=800,y=400)
        
        if v[0]==1:
            mf5 = tk.Label(root,text="Leg Workout:\n1.Quads Stretch\n2.Calves Stretch\n3.Calves Stretch\n4.Hamstrings Stretch\n5.Bodyweight Squat\n6.Forward Lunges\n7.Jump Squats\n8.Barbell Step Up\n9.Barbell Sumo Deadlift\n10.Barbell High Bar Squat",background="light yellow",foreground="Black",justify='left',font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf5.place(x=800,y=400)
        
        if v[0]==2:
            mf5 = tk.Label(root,text="Leg Workout:\n1.Quads Stretch\n2.Calves Stretch\n3.Hamstrings Stretch\n4.Bodyweight Squat\n5.Forward Lunges\n6.Jump Squats\n7.Barbell Step Up\n8.Barbell Sumo Deadlift\n9.Barbell High Bar Squat\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf5.place(x=800,y=400)
            
    def ABS():
        if v[0]==0:
            lf6 = tk.Label(root,text="ABS Workout:\n1.Abdominals Stretch\n2.Crunches\n3.Laying Leg Raises\n4.Hanging Knee Raises\n5.Cable Kneeling Crunch\n",background="light yellow",justify='left',foreground="Black",font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            lf6.place(x=800,y=400)
        
        if v[0]==1:
            mf6 = tk.Label(root,text="ABS Workout:\n1.Abdominals Stretch\n2.Crunches\n3.Laying Leg Raises\n4.Hanging Knee Raises\n5.Cable Kneeling Crunch\n6.Barbell Roll Outs\n7.Barbell Situp\n8.Cable Standing Crunch\n\n",background="light yellow",foreground="Black",justify='left',font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf6.place(x=800,y=400)
        
        if v[0]==2:
            mf6 = tk.Label(root,text="ABS Workout:\n1.Abdominals Stretch\n2.Crunches\n3.Laying Leg Raises\n4.Hanging Knee Raises\n5.Cable Kneeling Crunch\n6.Barbell Roll Outs\n7.Barbell Situp\n8.Cable Standing Crunch\n\n",background="light yellow",foreground="Black",justify='left',font=('times', 20, ' bold '),width=30,bd=4, relief="solid")
            mf6.place(x=800,y=400)
        
        
    
    def back():
        print('<')
        call(['python','Check_Prediction.py'])
    
    def home():
        print('Home')
        call(['python','GUI_Master.py'])
            
            
    
    photo = ImageTk.PhotoImage(image1)
    
    button4 = tk.Button(root, image=photo,font=('times', 2, ' bold '), command=home,background="black", bd=5, relief="solid")
    button4.place(x=1810, y=2)
    
    button3 = tk.Button(root, foreground="White", background="black",text="<",font=('times', 30, ' bold '), command = back,bd=3, relief="solid")
    button3.place(x=0, y=2)
    
    chest = tk.Button(root, foreground="black", background="antique white",text="Chest Workout",font=('times', 30, ' bold '),width= 20, command = chest,bd=3, relief="solid")
    chest.place(x=50,y=100)
    
    BackWorkout = tk.Button(root, foreground="black", background="antique white",text="Back Workout",font=('times', 30, ' bold '),width= 20, command = backWorkout,bd=3, relief="solid")
    BackWorkout.place(x=50,y=250)
    
    arm = tk.Button(root, foreground="black", background="antique white",text="Arm Workout",font=('times', 30, ' bold '),width= 20, command = Arm,bd=3, relief="solid")
    arm.place(x=50,y=400)
    
    shoulders = tk.Button(root, foreground="black", background="antique white",text="Shoulders Workout",font=('times', 30, ' bold '),width= 20, command = Shoulders,bd=3, relief="solid")
    shoulders.place(x=50,y=550)
    
    
    leg = tk.Button(root, foreground="black", background="antique white",text="Leg Workout",font=('times', 30, ' bold '),width= 20, command = legs,bd=3, relief="solid")
    leg.place(x=50,y=700)
    
    ABS = tk.Button(root, foreground="black", background="antique white",text="ABS Workout",font=('times', 30, ' bold '), width= 20,command = ABS,bd=3, relief="solid")
    ABS.place(x=50,y=850)
    
    
    
    root.mainloop()
    
    
train()