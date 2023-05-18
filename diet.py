import tkinter as tk
import numpy as np
import pandas as pd
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from subprocess import call
from joblib import dump, load
import tempfile
import sqlite3
import numpy as np
from tkinter import messagebox as ms
import tkinter.font as tkFont
from PIL import ImageTk, Image
from PIL import Image, ImageTk, ImageFilter


def Train():
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    #root.geometry("1700x1500+250+5")
    root.title("Body Fitness Prediction")
    root.configure(background="white")
    label = tk.Label(root, text="Diet Plan")
    image = Image.open("diet.jpg")
    image = image.resize((2000, 1000), Image.ANTIALIAS)
    image = image.filter(ImageFilter.BLUR)
    background_image = ImageTk.PhotoImage(image)

    # Create a label widget and set the image as the background
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0)

    label.pack()
    
    e1 = tk.IntVar()
    e2 = tk.StringVar()
    e3 = tk.IntVar()
    e4 = tk.IntVar()
    e5 = tk.IntVar()
    e6 = tk.IntVar()
    e7 = tk.IntVar()
    e8 = tk.IntVar()
    e9 = tk.IntVar()
    e10 = tk.IntVar()
    e11 = tk.IntVar()
    
    with open("example.txt", "r") as f:
        input_data = f.read()
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11= map(int, input_data.strip().split(','))
    
    
    
    from joblib import dump , load
    a1=load('DT.joblib')
    v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
    print(v)
    lbl = tk.Label(root, text="Diet Plan", font=('times', 40,' bold '), height=1, width=60,bg="black",fg="white",bd=10, relief="solid")
    lbl.place(x=0, y=2)
    

    if v[0] == 0:
        a1=load('DT.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
        #print("Breakfast: Oats Banana Pancakes with Protein Shake \n\n\n Lunch: \nMultigrain roti along with palak chicken and Avocado bell pepper salad \n\n\n Pre-Workout: Snack	Bananas \n\n\n Dinner: Brown rice\npeas paneer curry\nsprouts vegetable salad \n")
        ld1 = tk.Label(root,text="1. Breakfast:\n\tBananas\n\tProtein Shake\n\tOats Banana Pancakes with Protein Shake\n\n2. Lunch:\n\tMultigrain roti along with palak chicken\n\tAvocado bell pepper salad\n\n3. Pre-Workout Snack:\n\tBananas\n\tProtein Shake\n\tMass Gainer \n\n4. Dinner: \n\tBrown rice\n\tPeas Paneer Curry\n\tSprouts vegetable salad \n ",background="light goldenrod",justify='left',foreground="black",font=('times', 20, ' bold '), bd=4, relief="solid",width=40)
        ld1.place(x=700,y=250)
        
        

    if v[0]== 1:
        a1=load('DT.joblib')    
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
        #print("Breakfast:- Scrambled Egg Whole Grain Toast Smoothie \n\n\n Lunch:- Grilled chicken vegetable roti rolls \nGreen Salad \n\n\n Pre-Workout Snack:- Mixed Nuts & Dried Fruits\n\n\n Dinner(Post-Workout):-Chicken Stir Fry\nSpring Onion,\n Peppers & Broccoli\nChocolate Milk\n")
        
        md1 = tk.Label(root,text="1. Breakfast:\n\tBananas\n\tProtein Shake\n\tScrambled Egg Whole Grain Toast Smoothie\n\n2. Lunch:\n\tGrilled chicken vegetable roti rolls\n\tGreen Salad\n\n\n3. Pre-Workout Snack: \n\tMixed Nuts & Dried Fruits\n\tProtein Shake\n\tMass Gainer\n\n4. Dinner(Post-Workout):\n\tChicken Stir Fry\n\tSpring Onion,\n\tPeppers & Broccoli\n\tChocolate Milk ",background="light goldenrod",justify='left',foreground="black",font=('times', 20, ' bold '), bd=4, relief="solid")
        
        md1.place(x=700,y=250)
        
            
    if v[0] == 2:
        a1=load('DT.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
        #print("Breakfast:- Oatmeal with Nuts Smoothie \n Lunch:-Whole wheat pasta with chicken and Green Salad\n Pre-Workout Snack:- Granola or Cereal\n  Dinner(Post-Workout):-Fish curry, boiled green peas salad\n Brown Rice, Garden Peas,Milk")
        pd1 = tk.Label(root,text="1. Breakfast:\n\tBananas\n\tProtein Shake\n\tOatmeal with Nuts Smoothie\n\n2. Lunch:\n\tWhole wheat pasta with chicken and Green Salad\n\n3. Pre-Workout Snack:\n\tGranola or Cereal\n\tBananas\n\tProtein Shake\n\n4. Dinner(Post-Workout):\n\tFish curry\n\tboiled green peas salad\n\tBrown Rice\n\tGarden Peas\n\tMilk",background="light goldenrod",justify='center',foreground="black",font=('times', 20, ' bold '), bd=4, relief="solid")
        pd1.place(x=700,y=250)
        
                

                
            
    def back():
        print('<')
        call(['python','Check_Prediction.py'])
            
   
    def home():
        print('Home')
        call(['python','GUI_Master.py'])
            
    image1 = Image.open("home_button.png")
    image1 = image1.resize((105, 60), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image1)
    
    button4 = tk.Button(root, image=photo,font=('times', 2, ' bold '), command=home,background="black", bd=5, relief="solid")
    button4.place(x=1810, y=2)
    
    button3 = tk.Button(root, foreground="White", background="black",text="<",font=('times', 30, ' bold '), command = back,bd=3, relief="solid")
    button3.place(x=0, y=2)
    root.mainloop()
Train()


