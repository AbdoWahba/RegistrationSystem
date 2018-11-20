from tkinter import *
from tkinter import font
from tkinter import ttk

from PIL import Image, ImageTk

import json


class Application:
    def __init__(self, master):

        master.title("ACES Expo Registration'19")
        master.configure(background='#ededed')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#ffffff')
        self.style.configure('TButton', background='#009b45',
                             foreground='#ffffff', relief='flat')
        self.style.configure('TCombobox', background='#ffffff')
        self.style.configure('TLabel', background='#ffffff',
                             font=('Helvetica', 14))
        self.style.configure('Header.TLabel', font=('Times', 24))

        self.frame = ttk.Frame(master)
        self.frame.place(relx=0.5, anchor='n', relwidth=0.3)

        # Header frame
        self.frame_header = ttk.Frame(self.frame)
        self.frame_header.pack(pady=(20, 50))

        self.logo_img = ImageTk.PhotoImage(Image.open("acesLogo.png"))
        ttk.Label(self.frame_header,
                  image=self.logo_img).pack()

        ttk.Label(self.frame_header, text="ACES Expo Registration'19",
                  style='Header.TLabel').pack(pady=(10, 0))

        # Form frame
        self.frame_form = ttk.Frame(self.frame)
        self.frame_form.pack(fill=BOTH, expand=1)

        # Days label
        ttk.Label(self.frame_form, text="Booth Day:").pack(fill=X, expand=1,
                                                           pady=(10, 2), padx=10)

        # Combo Box
        self.days_var = IntVar()
        days = (1, 2, 3, 4, 5, 6)
        days_combo = ttk.Combobox(self.frame_form, values=days,
                                  state="readonly", height=6,
                                  textvariable=self.days_var)
        days_combo.set(1)
        days_combo.pack(fill=X, expand=1, padx=10)

        # Email label
        ttk.Label(self.frame_form, text="Email:").pack(fill=X, expand=1,
                                                       pady=(200, 2), padx=10)

        # Email entry
        self.email_var = StringVar()
        self.entry_email = ttk.Entry(self.frame_form,
                                     textvariable=self.email_var,
                                     font=('Arial', 10))
        self.entry_email.pack(fill=X, expand=1, padx=10)

        # Submit button
        # ttk.Style().configure("TButton", relief="flat",
        #                       background="#00ff00")
        btn = ttk.Button(self.frame_form, text="Save", command=self.submit)
        btn.pack(pady=(300, 80))

    # Submit the email to txt file
    def submit(self):
        email = str(self.email_var.get())
        day = self.days_var.get()

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
root.geometry('1300x500+200+200')
app = Application(master=root)
root.mainloop()
