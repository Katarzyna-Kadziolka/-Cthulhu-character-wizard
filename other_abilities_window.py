from tkinter import *

import abilities_window
from ability import Ability
from base_window import BaseWindow
from data import Data
from random_calculator import RandomCalculator


class OtherAbilitiesWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.calculator = RandomCalculator()
        self.create_content()

    def create_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        frame_1 = Label(self.frame)
        frame_1.grid(row=0, column=0)
        frame_2 = Label(self.frame)
        frame_2.grid(row=1, column=0, pady=10)
        frame_3 = Label(self.frame)
        frame_3.grid(row=2, column=0, pady=10)

        #frame_1
        label_title = Label(frame_1, text="Pozostałe cechy", font=("Helvetica", 11)).grid(row=0, column=0, pady=10)

        #frame_2
        label_move_rate = Label(frame_2, text="Szybkość:").grid(row=0, column=0, sticky=E, padx=10)
        label_hp = Label(frame_2, text="Wytrzymałość:").grid(row=1, column=0, sticky=E, padx=10)
        label_sanity = Label(frame_2, text="Poczytalność:").grid(row=2, column=0, sticky=E, padx=10)
        label_magic_points = Label(frame_2, text="Punkty magii:").grid(row=0, column=2, sticky=E, padx=10)
        label_build = Label(frame_2, text="Postura:").grid(row=1, column=2, sticky=E, padx=10)
        label_damage_bonus = Label(frame_2, text="Modyfikator obrażeń:").grid(row=2, column=2, sticky=E, padx=10)

        sv_move_rate = StringVar()
        sv_move_rate.trace("w", lambda name, index, mode, sv=sv_move_rate: Data.save_data(sv, Ability.MOVE_RATE))
        sv_hp = StringVar()
        sv_hp.trace("w", lambda name, index, mode, sv=sv_hp: Data.save_data(sv, Ability.HP))
        sv_sanity = StringVar()
        sv_sanity.trace("w", lambda name, index, mode, sv=sv_sanity: Data.save_data(sv, Ability.SANITY))
        sv_magic_points = StringVar()
        sv_magic_points.trace("w", lambda name, index, mode, sv=sv_magic_points: Data.save_data(sv, Ability.MAGIC_POINTS))
        sv_build = StringVar()
        sv_build.trace("w", lambda name, index, mode, sv=sv_build: Data.save_data(sv, Ability.BUILD))
        sv_damage_bonus = StringVar()
        sv_damage_bonus.trace("w", lambda name, index, mode, sv=sv_damage_bonus: Data.save_data(sv, Ability.DAMAGE_BONUS))


        self.entry_move_rate = Entry(frame_2, textvariable=sv_move_rate, width=5)
        self.entry_hp = Entry(frame_2, textvariable=sv_hp, width=5)
        self.entry_sanity = Entry(frame_2, textvariable=sv_sanity, width=5)
        self.entry_magic_points = Entry(frame_2, textvariable=sv_magic_points, width=5)
        self.entry_build = Entry(frame_2, textvariable=sv_build, width=5)
        self.entry_damage_bonus = Entry(frame_2, textvariable=sv_damage_bonus, width=5)


        self.entry_move_rate.grid(row=0, column=1)
        self.entry_hp.grid(row=1, column=1)
        self.entry_sanity.grid(row=2, column=1)
        self.entry_magic_points.grid(row=0, column=3)
        self.entry_build.grid(row=1, column=3)
        self.entry_damage_bonus.grid(row=2, column=3)

        # frame_3

        btn_next_window = Button(frame_3, text="Dalej", width=10, command=self.next_window).grid(
            row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_3, text="Cofnij", width=10, command=self.previous_window).grid(
            row=0, column=0, pady=20, padx=50, stick=W)

        self.insert_move_rate()
        self.insert_hp()

    def insert_move_rate(self):
        strength = int(Data.data[Ability.STRENGTH])
        dexterity = int(Data.data[Ability.DEXTERITY])
        size = int(Data.data[Ability.SIZE])
        age = int(Data.data["age"])
        self.set_text(self.entry_move_rate, self.calculator.get_move_rate(strength, dexterity, size, age))
        self.entry_move_rate.config(state=DISABLED)

    def insert_hp(self, entry_hp):
        #TODO kontynuuj
        pass


    def previous_window(self):
        self.frame.destroy()
        abilities_window.AbilitiesWindow(self.root)

    def next_window(self):
        self.frame.destroy()