from tkinter import *
from PIL import ImageTk,Image
import random

# main
window = Tk()
window.geometry("400x360")
#window.configure(bg = "#F0F8FF")
window.title("Guess Game")

my_list = ["__","__","__"]
values = [".", "X", "."]
num = [1, 2, 3]

def myClick():
   global myLabel
   random.shuffle(values)
   dic_list = dict(zip(num, values))
   choice = entry4.get()

   entry["state"] = NORMAL
   entry2["state"] = NORMAL
   entry3["state"] = NORMAL

   entry.insert(0,dic_list[1])
   entry2.insert(0,dic_list[2])
   entry3.insert(0,dic_list[3])

   if dic_list[int(choice)] == "X":
       canvas.itemconfig(image_container, image = new_image2)
       canvas.pack()
       disabled()
   else:
       canvas.itemconfig(image_container, image = new_image3)
       canvas.pack()
       disabled()

   entry4.insert(0, "Type your selection (1,2,3)")
   entry4.configure(state=DISABLED)

def disabled():
   myButton2["state"] = DISABLED

def active():
   myButton2["state"] = ACTIVE

def myClick2():

   entry.delete(0, END)
   entry2.delete(0, END)
   entry3.delete(0, END)

   canvas.itemconfig(image_container, image = new_image)
   canvas.pack()
   entry4.delete(0,END)

   active()

   entry["state"] = DISABLED
   entry2["state"] = DISABLED
   entry3["state"] = DISABLED

   entry4["state"] = NORMAL
   entry4.delete(0, END)

def on_click(event):
   entry4.configure(state = NORMAL)
   entry4.delete(0, END)
   # make the callback only work once
   entry4.unbind("<Button-1>", on_click_id)
   myButton2["state"] = ACTIVE

canvas = Canvas(window, width = 300, height = 120, bg = "black")
canvas.pack()

image1 = Image.open("C:/Users/Buse Çalışır/OneDrive/Masaüstü/let's Play.png")
resized = image1.resize((500,800))
new_image = ImageTk.PhotoImage(resized)

image_container = canvas.create_image(0, 0, anchor = NW, image = new_image)

image2 = Image.open("C:/Users/Buse Çalışır/OneDrive/Masaüstü/congratulations.png")
resized2 = image2.resize((512, 800))
new_image2 = ImageTk.PhotoImage(resized2)

image3 = Image.open("C:/Users/Buse Çalışır/OneDrive/Masaüstü/game over.png")
resized3 = image3.resize((660,990))
new_image3 = ImageTk.PhotoImage(resized3)

entry = Entry(window, width = 5, state = DISABLED)
entry.place(x = 150, y = 140)

entry2 = Entry(window, width = 5, state = DISABLED)
entry2.place(x = 190, y = 140)

entry3 = Entry(window, width = 5, state = DISABLED)
entry3.place(x = 230, y = 140)

entry4 = Entry(window, width = 23)
entry4.place(x = 140, y = 180)
entry4.insert(0, "Type your selection (1,2,3)")
entry4.configure(state = DISABLED)

on_click_id = entry4.bind("<Button-1>", on_click)

myButton2 = Button(window, text = "Open", padx = 30, pady = 10, command = myClick, fg = "purple", bg = "#8DB600", state = DISABLED)
myButton2.place(x = 160, y = 220)

myButton3 = Button(window, text = "Clean", padx = 30, pady = 10, command = myClick2, fg = "#960018", bg = "#89CFF0")
myButton3.place(x = 160, y = 290)

# run the main loop
window.mainloop()
