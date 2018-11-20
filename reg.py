from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'white'
        self.pack(expand=True, fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        self.logo_img = ImageTk.PhotoImage(Image.open("acesLogo.png"))
        self.logo = Label(self, image=self.logo_img, bd=0)
        self.logo.place(relx=0.5, y=15, anchor='n')

        self.day_label = ttk.Label(text="Booth Day", background='white')
        self.day_label.place(relx=0.5, rely=0.5, anchor='center')


root = Tk()
root.geometry('640x480+200+200')
app = Application(master=root)
app.mainloop()
