
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import tkinter as tk

def Train():
    root = tk.Tk()
    root.geometry('600x200')
    # Global Variables
    FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 100)
    FONT_COLOR = "Black"
    names = tk.StringVar()

    # Placing it in the center, then making some adjustments.

    def make_certificates():
        '''Function to save certificates as a .png file'''
        nonlocal draw  # Use the draw variable from the enclosing scope
        names_str = names.get()
        name_width, name_height = draw.textsize(names_str, font=FONT_FILE)
        draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), names_str, fill=FONT_COLOR, font=FONT_FILE)
        image_source.save("./out/" + names_str + "'s.png")
        print("Saving Certificate of: " + names_str + "'s Certificate")
        image_source.show()

    l1 = tk.Label(root, text="Name", background="white", font=('times', 20, ' bold '), width=10)
    l1.place(x=5, y=30)
    names_entry = tk.Entry(root, bd=2, width=20, font=("TkDefaultFont", 20), textvar=names)
    names_entry.place(x=200, y=30)

    button1 = tk.Button(root, foreground="white", background="black", text="Submit", command=make_certificates,
                        font=('times', 20, ' bold '), width=10, bd=4, borderwidth=7, relief="sunken")
    button1.place(x=130, y=90)

    template = Image.open(r'certificate1.png')
    WIDTH, HEIGHT = template.size

    image_source = Image.open(r'certificate1.png')
    draw = ImageDraw.Draw(image_source)

    root.mainloop()

Train()