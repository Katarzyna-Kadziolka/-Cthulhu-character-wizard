from tkinter import *
import occupation_info_extractor
import occupations_window
import random_calculator
from Enums.ability import Ability
from base_window import BaseWindow
from data import Data
from occupation_info import OccupationInfo


class OccupationSelectWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.calculator = random_calculator.RandomCalculator()
        self.get_full_occupation_info()
        self.create_content()


    def create_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)

        frame_1 = Label(self.frame)
        frame_2 = Label(self.frame)
        frame_3 = Label(self.frame)
        frame_4 = Label(self.frame)

        frame_1.grid(row=0, column=0)
        frame_2.grid(row=1, column=0)
        frame_3.grid(row=2, column=0)
        frame_4.grid(row=3, column=0)

        occupation_info = self.get_full_occupation_info()
        #frame_1
        label_title = Label(frame_1, text=occupation_info.occupation_pl, font=("Helvetica", 16)).grid(row=0, column=0, pady=20)

        #frame_2
        label_intelligence_points = Label(frame_2, text=f"Punkty personalne: ")
        label_occupation_points = Label(frame_2, text=f"Punkty zawodowe: {Data.data['occupation_skill_points']}")
        label_credit_rating = Label(frame_2, text=f"Majętność: ")
        label_intelligence_points.grid(row=0, column=0)
        label_occupation_points.grid(row=1, column=0)
        label_credit_rating.grid(row=2, column=0)

        #frame_3
        label_skills_title = Label(frame_3, text="Umiejętności zawodowe", font=("Helvetica", 12))
        label_skills = Label(frame_3, text="")
        label_skills_title.grid(row=0, column=0, pady=20)
        label_skills.grid(row=1, column=0)

        #frame_4
        btn_next_window = Button(frame_4, text="Dalej", width=10, command=self.next_window).grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_4, text="Cofnij", width=10, command=self.previous_window).grid(row=0, column=0, pady=20, padx=50, stick=W)


    def get_full_occupation_info(self) -> OccupationInfo:
        infos = occupation_info_extractor.get_infos()
        #infos = lista klas
        self.info = [i for i in infos if i.occupation_pl == Data.data["occupation"]][0]
        #info = pojedyncza klasa
        abilities = {
            Ability.POWER: Data.data[Ability.POWER],
            Ability.CONDITION: Data.data[Ability.CONDITION],
            Ability.SIZE: Data.data[Ability.SIZE],
            Ability.DEXTERITY: Data.data[Ability.DEXTERITY],
            Ability.STRENGTH: Data.data[Ability.STRENGTH],
            Ability.INTELLIGENCE: Data.data[Ability.INTELLIGENCE],
            Ability.EDUCATION: Data.data[Ability.EDUCATION],
            Ability.APPEARANCE: Data.data[Ability.APPEARANCE]
        }

        Data.data["occupation_skill_points"] = self.calculator.get_occupation_skills_points(self.info.occupation_skills_points, abilities)

        return self.info

    def next_window(self):
        self.frame.destroy()

    def previous_window(self):
        self.frame.destroy()
        occupations_window.OccupationsWindow(self.root)