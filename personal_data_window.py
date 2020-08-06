from tkinter import *
import random
from abilities_window import AbilitiesWindow
from base_window import BaseWindow
from data import Data
import home_window
from database import Database
from random_calculator import RandomCalculator


class PersonalDataWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.entry_list = []
        self.create_content()
        self.database = Database()
        self.calculator = RandomCalculator()

    def create_content(self):

        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        sv_f_name = StringVar()
        sv_f_name.trace("w", lambda name, index, mode, sv=sv_f_name: self.entry_changed(sv, "first_name"))
        sv_l_name = StringVar()
        sv_l_name.trace("w", lambda name, index, mode, sv=sv_l_name: self.entry_changed(sv, "last_name"))
        sv_age = StringVar()
        sv_age.trace("w", lambda name, index, mode, sv=sv_age: self.entry_changed(sv, "age"))

        label_f_name = Label(self.frame, text="Imię:").grid(row=0, column=0, stick=E)
        label_l_name = Label(self.frame, text="Nazwisko:").grid(row=1, column=0, stick=E)
        label_age = Label(self.frame, text="Wiek:").grid(row=2, column=0, stick=E)
        label_gender = Label(self.frame, text="Płeć:").grid(row=3, column=0, stick=E)

        self.e_f_name = Entry(self.frame, textvariable=sv_f_name)
        self.e_l_name = Entry(self.frame, textvariable=sv_l_name)
        self.e_age = Entry(self.frame, textvariable=sv_age)

        self.e_f_name.grid(row=0, column=1, columnspan=2, padx=10)
        self.e_l_name.grid(row=1, column=1, columnspan=2, padx=10)
        self.e_age.grid(row=2, column=1, columnspan=2, padx=10)

        self.entry_list.append(self.e_f_name)
        self.entry_list.append(self.e_l_name)
        self.entry_list.append(self.e_age)

        self.radio_var = StringVar()
        self.radio_var.trace("w", lambda name, index, mode, sv=self.radio_var: Data.save_data(sv, "gender"))
        self.radio_var.set("female")
        self.radio = Radiobutton(self.frame, text="M", variable=self.radio_var, value="male").grid(row=3, column=1, pady=5,
                                                                              sticky=W + E + N + S)
        self.radio = Radiobutton(self.frame, text="K", variable=self.radio_var, value="female").grid(row=3, column=2, pady=5, sticky=W)

        self.btn_third_window = Button(self.frame, text="Dalej", width=10, state=DISABLED, command=self.next_window)
        self.btn_third_window.grid(row=4, column=2,pady=20, stick=E)
        btn_back = Button(self.frame, text="Cofnij", width=10, command=self.previous_window)\
            .grid(row=4, column=0, pady=20, stick=W)
        btn_random_names = Button(self.frame, text="Random", command=lambda: self.set_random_personal_data())\
            .grid(row=5, column=0, columnspan=3, pady=5, stick=W + E + N + S)

    def entry_changed(self, sv, name):
        Data.save_data(sv, name)
        self.check_fill_entry(self.btn_third_window, self.entry_list)
        if sv.get() == self.e_age.get():
            self.is_number(sv)

    def is_number(self, sv):
        try:
            int(sv.get())
        except ValueError:
            self.btn_third_window.config(state=DISABLED)

    def next_window(self):
        self.frame.destroy()
        AbilitiesWindow(self.root)

    def previous_window(self):
        self.frame.destroy()
        home_window.HomeWindow(self.root)

    def set_random_personal_data(self):
        self.radio_var.set(self.calculator.get_random_gender())
        self.set_text(self.e_f_name, self.calculator.get_random_name(self.radio_var.get()))
        self.set_text(self.e_l_name, self.calculator.get_surname())
        self.set_text(self.e_age, self.calculator.get_age())

