from Tkinter import *
import Tkinter as tk
import tkFileDialog
import matplotlib
matplotlib.use("Svg")

import matplotlib.pyplot as plt
from matplotlib.patches import Shadow
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk
import sys

root = Tk()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="add command here")
   button.pack()
   
root.geometry("920x720")
root.title("C3 GG")

def close_window():
    root.destroy()

def run():
   exec(open("C:\\Users\\Samski\\Desktop\\Hackothn\\Hackathon\\gui.py").read())

def find():
    drawing = svg2rlg("svg_filter_pie.svg")
    #renderPDF.drawToFile(drawing, "file.pdf")
    renderPM.drawToFile(drawing, "file.png")
############### Input ##############################
def callback(userID):
    print userID.widget.get()

L1 = Label(root, text="Social Security")
L1.pack()
L1.place(x=220, y=100)
d = tk.Entry(root)
d.pack()
d.place(x=300, y=100)
# Calling on_change when you press the return key
d.bind("<Return>", callback)

    
############### Open Image #############################
def pic():
    toplevel = Toplevel()
    filename = ("file.png")
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    label = Label(toplevel,image=photo)
    label.image = photo # keep a reference!
    label.pack()

################# Add File ##############################
def choose_files():

    Tkinter.Tk().withdraw() # Close the root window
    in_path = tkFileDialog.askopenfilename()
    print in_path

if __name__ == "__choose_files__":
    main()


################# Menu Bars ##############################
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=choose_files)
filemenu.add_command(label="Open", command=choose_files)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=close_window)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

############################################################

a = Button(root, text = "Run file", width=20, height=3, command = run)
a.pack()
a.place(x=20, y=20)

b = Button(root, text = "Open file", width=20, height=3, command = find)
b.pack()
b.place(x=20, y=80)

c = Button(root, text = "Open Pic", width=20, height=3, command = pic)
c.pack()
c.place(x=20, y=140)

#d = Button(root, text="Send", width=20,height=3, command=callback)
#d.pack()
#d.place(x=20, y=240)

e = Button(root, text="Exit", width=20,height=3, command=close_window)
e.pack()
e.place(x=20, y=300)

root.config(menu=menubar)

root.mainloop()
