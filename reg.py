from tkinter import *
from tkinter import font
from tkinter import ttk

from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['bg'] = 'white'
        self.pack(expand=True, fill=BOTH)

        title_font = font.Font(family="Times", size=24)
        font1 = font.Font(family="Helvetica", size=14)
        style = ttk.Style()
        # style.theme_settings("default", {
        #     "TCombobox": {
        #         "configure": {"padding": 5},
        #         "map": {
        #             "background": [("active", "green2"),
        #                            ("!disabled", "green4")],
        #             "fieldbackground": [("!disabled", "green3")],
        #             "foreground": [("focus", "OliveDrab1"),
        #                            ("!disabled", "OliveDrab2")]
        #         }
        #     }
        # })

        self.frame = ttk.Frame(self)
        self.frame.place(relx=0.5, anchor='n', relwidth=0.3)
        # self.frame.config(style='frame.TFrame')

        self.frame_header = ttk.Frame(self.frame)
        self.frame_header.pack(fill=X, expand=1)

        self.logo_img = ImageTk.PhotoImage(Image.open("acesLogo.png"))
        Label(self.frame_header, image=self.logo_img, bd=0,
              bg='white').pack(fill=X, expand=1)

        Label(self.frame_header, text="ACES Expo Registration'19",
              bd=0, bg='white', pady=10, font=title_font).pack(fill=X, expand=1)

        self.frame_form = ttk.Frame(self.frame)
        self.frame_form.pack(fill=X, expand=1)

        ttk.Label(self.frame_form, text="Booth Day:",
                  background='white', font=font1).pack(fill=X, expand=1)

        self.days_value = StringVar()
        days = ('Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6')
        days_combo = ttk.Combobox(self.frame_form, values=days,
                                  state="readonly", height=6,
                                  textvariable=self.days_value)
        days_combo.pack(fill=X, expand=1)

        ttk.Label(self.frame_form, text="Email:",
                  background='white', font=font1).pack(fill=X, expand=1)

        self.entry_email = ttk.Entry(self.frame_form)
        self.entry_email.pack(fill=X, expand=1)


root = Tk()
root.geometry('640x480+200+200')
app = Application(master=root)
app.mainloop()
