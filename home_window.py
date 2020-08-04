from tkinter import *
from tkinter import messagebox
from base_window import BaseWindow
from personal_data_window import PersonalDataWindow


class HomeWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)

        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.create_content()

    def create_content(self):
        btn_second_window = Button(self.frame, text="Stwórz postać krok po kroku",command=self.next_window).grid(row=0, column=0, pady=2, sticky=W + E + N + S)
        btn_random_charackter = Button(self.frame, text="Wygeneruj losową postać", command=None).grid(row=1, column=0, pady=2, stick=W + E + N + S)
        btn_close = Button(self.frame, text="Zamknij", command=self.close_program).grid(row=2, column=0, pady=2, stick=W + E + N + S)

    def close_program(self):
        answer = messagebox.askyesno(title="Zamknij", message="Czy na pewno zamknac?")
        if answer > 0:
            self.root.destroy()
            sys.exit()

    def next_window(self):
        self.frame.destroy()
        PersonalDataWindow(self.root)