from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Body Fitness Prediction")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

img=ImageTk.PhotoImage(Image.open("B16.jpg"))

img2=ImageTk.PhotoImage(Image.open("B15"))

img3=ImageTk.PhotoImage(Image.open("b17.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
def move():
 	global x
 	if x == 4:
	   x = 1
 	if x == 1:
	   logo_label.config(image=img)
 	elif x == 2:
	   logo_label.config(image=img2)
 	elif x == 3:
	   logo_label.config(image=img3)
 	x = x+1
 	root.after(2000, move)

# calling the function
move()
 # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Body Fitness Prediction", font=('times', 35,' bold '), height=1, width=70,bg="black",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"training.csv")



data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv(r"training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['age'] = le.fit_transform(data['age'])
    
    data['gender'] = le.fit_transform(data['gender'])
    
    data['height_cm'] = le.fit_transform(data['height_cm'])

    data['weight_kg'] = le.fit_transform(data['weight_kg'])
    
    data['body fat_%'] = le.fit_transform(data['body fat_%'])
    
    data['diastolic'] = le.fit_transform(data['diastolic'])
    
    data['systolic'] = le.fit_transform(data['systolic'])
    
    data['gripForce'] = le.fit_transform(data['gripForce'])
    
    data['sit and bend forward_cm'] = le.fit_transform(data['sit and bend forward_cm'])
    
    data['sit-ups counts'] = le.fit_transform(data['sit-ups counts'])
    
    data['broad jump_cm'] = le.fit_transform(data['broad jump_cm'])
   
  

    """Feature Selection => Manual"""
    x = data.drop(['class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['class']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=213, y=85)


def Model_Training():
    data = pd.read_csv(r"training.csv")
    data.head()

    data = data.dropna()


    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['age'] = le.fit_transform(data['age'])
    
    data['gender'] = le.fit_transform(data['gender'])
    
    data['height_cm'] = le.fit_transform(data['height_cm'])

    data['weight_kg'] = le.fit_transform(data['weight_kg'])
    
    data['body fat_%'] = le.fit_transform(data['body fat_%'])
    
    data['diastolic'] = le.fit_transform(data['diastolic'])
    
    data['systolic'] = le.fit_transform(data['systolic'])
    
    data['gripForce'] = le.fit_transform(data['gripForce'])
    
    data['sit and bend forward_cm'] = le.fit_transform(data['sit and bend forward_cm'])
    
    data['sit-ups counts'] = le.fit_transform(data['sit-ups counts'])
    
    data['broad jump_cm'] = le.fit_transform(data['broad jump_cm'])
  
    

    """Feature Selection => Manual"""
    x = data.drop(['class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['class']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1234)

    #from sklearn.ensemble  import RandomForestRegressor
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as DT.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"DT.joblib")
    print("Model saved as DT.joblib")
    
    
    
def login():
    call(['python','gui_main.py'])
    
   


def call_file():
    call(['python','Check_Prediction.py'])


def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=20, y=90)

button3 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 17, "bold"),
                    text="Login Page", command=login, width=20, height=2)
button3.place(x=20, y=170)

button4 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 17, "bold"),
                    text=" Prediction", command=call_file, width=20, height=2)
button4.place(x=20, y=258)
exit = tk.Button(root, text="Exit", command=window, width=20, height=2, font=('times', 18, ' bold '),bg="red",fg="white")
exit.place(x=20, y=345)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''