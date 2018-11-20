from Tkinter import *
import json
from PIL import ImageTk, Image
import tkFont

def submit():
   email = str(emailVar.get())
   day = dayVar.get()

   email = email.lower()
   thisdict = {
        "email": email,
        "day": day,
        }
   myJson = json.dumps(thisdict)

   with open("reg.txt", mode='r+') as reg:
       if email in reg.read():
          print("sorry, this email has been regestered")
       else:
          reg.write(myJson)
          reg.write(",\n")




root = Tk()

font1 = tkFont.Font(family="Times", size="24")

body = Frame(root, bg="white")
body.pack(fill=BOTH, expand=True)

img = ImageTk.PhotoImage(Image.open("acesLogo.png"))
logo = Label(body, image=img, bd=0)
logo.pack()

title = Label(body, text="ACES Expo Registration'19", bg="white", bd=0, font=font1, pady=20)
title.pack()


labelFrame1 = Frame(body)
labelFrame1.pack()

menuFrame = Frame(body)
menuFrame.pack()

labelFrame2 = Frame(body)
labelFrame2.pack()

entryFrame = Frame(body)
entryFrame.pack()

bottomFrame = Frame(body)
bottomFrame.pack(side=BOTTOM)



L1 = Label(labelFrame1, text="Booth Day:", bg="white", bd=0)
L1.pack(side=LEFT)

mb =  Menubutton (menuFrame, text="Day", relief=RAISED)
mb.pack(side=LEFT)
mb.menu =  Menu (mb, tearoff=0)
mb["menu"] =  mb.menu

dayVar = IntVar()

mb.menu.add_radiobutton(label="1", variable=dayVar)
mb.menu.add_radiobutton(label="2", variable=dayVar)
mb.menu.add_radiobutton(label="3", variable=dayVar)
mb.menu.add_radiobutton(label="4", variable=dayVar)
mb.menu.add_radiobutton(label="5", variable=dayVar)
mb.menu.add_radiobutton(label="6", variable=dayVar)

mb.pack(side=LEFT)

L2 = Label(labelFrame2, text="Email:", bg="white", bd=0)
L2.pack(side=LEFT)

emailVar = StringVar()

E1 = Entry(entryFrame, width=40, textvariable=emailVar, bg="white")
E1.pack(side=LEFT)

B = Button(bottomFrame, text="Submit", command=submit)
B.pack(side=BOTTOM)

root.mainloop()
