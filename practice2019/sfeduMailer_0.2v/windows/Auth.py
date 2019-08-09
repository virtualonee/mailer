from tkinter import *
from . InputTitleAndText import InputTitleAndText
from tkinter import Tk, Label, Button, Text, Entry

class Authorization:
    def __init__(self, master):
        self.master = master
        master.title("SfeduMailer Вход")

        self.labelLogin = Label(master, text="Почта")
        self.labelLogin.place(x=130, y=20)

        self.addr_fromText = Text(master, height=1, width=23)
        self.addr_fromText.place(x=50, y=50)
        self.addr_fromText.insert(INSERT, "publish2018@mail.ru")

        self.labelPass = Label(master, text="Пароль")
        self.labelPass.place(x=130, y=80)

        self.passwordText = ""
        self.passEntry = Entry(master, textvariable=self.passwordText, show='*', )
        self.passEntry.place(x=50, y=110)

        self.greet_button = Button(master, text="Войти", width=15, height=2, command=self.EnterInInputTitleAndTextWindow)
        self.greet_button.place(x=80, y=200 - 50)

    def EnterInInputTitleAndTextWindow(self):
        login = self.addr_fromText.get(1.0, END)

        password = self.passEntry.get()
        self.master.destroy()
        root = Tk()
        root.geometry('300x200+200+100')
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
        root.wm_geometry("+%d+%d" % (x, y))
        root.resizable(width=False, height=False)
        my_gui = InputTitleAndText(root, login, password)
        root.mainloop()
