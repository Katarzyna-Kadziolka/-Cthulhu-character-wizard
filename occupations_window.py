import random
from tkinter import *
import occupation_info_extractor
import occupation_select_window
import other_abilities_window
import translator
from base_window import BaseWindow
from data import Data


class OccupationsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.create_content()

    def create_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        frame_1 = Label(self.frame)
        frame_1.grid(row=0, column=0)
        frame_2 = Label(self.frame)
        frame_2.grid(row=1, column=0)
        frame_3 = Label(self.frame)
        frame_3.grid(row=2, column=0)

        #frame_1
        label_title = Label(frame_1, text="Wybór zawodu", font=("Helvetica", 16)).grid(row=0, column=0, pady=20)

        #frame_2
        scrollbar = Scrollbar(frame_2)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(frame_2, yscrollcommand=scrollbar.set, selectmode=SINGLE)

        info = occupation_info_extractor.get_infos()
        self.occupation_names_pl = [i.occupation_pl for i in info]
        self.occupation_names_pl.sort()


        for i in self.occupation_names_pl:
            self.listbox.insert(END, i)

        self.listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.listbox.yview)

        #frame_3
        btn_next_window = Button(frame_3, text="Dalej", width=10, command=self.next_window).grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_3, text="Cofnij", width=10, command=self.previous_window).grid(row=0, column=0, pady=20, padx=50, stick=W)
        btn_random = Button(frame_3, text="Random", width=20, command=self.random_button_click).grid(row=1, column=0, columnspan=2, pady=5)

    def previous_window(self):
        self.frame.destroy()
        other_abilities_window.OtherAbilitiesWindow(self.root)

    def next_window(self):
        Data.data["occupation"] = [key for key, value in translator.Translator.occupations.items() if value == self.listbox.get(ACTIVE)][0]
        self.frame.destroy()
        occupation_select_window.OccupationSelectWindow(self.root)


    def random_button_click(self):
        self.listbox.select_clear(0, END)
        random_index = random.randint(0, len(self.occupation_names_pl)-1)
        self.listbox.activate(random_index)
        self.listbox.see(random_index)
        self.listbox.select_set(random_index)


