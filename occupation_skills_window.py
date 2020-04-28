from tkinter import *

import occupation_select_window
import random_calculator
import skill_formater
import skills_info
import translator
from Enums.ability import Ability
from base_window import BaseWindow
from data import Data


class OccupationSkillsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.calculator = random_calculator.RandomCalculator()
        self.skills_into = skills_info.SkillsInfo()
        self.skill_formater = skill_formater.SkillFormater()
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

        #frame_1
        label_title = Label(frame_1, text="Umiejętności zawodowe", font=("Helvetica", 16)).grid(row=0, column=0)

        #frame_2
        label_occupation_skill_points = Label(frame_2, text="Dostępne punkty zawodowe: ").grid(row=0, column=0)
        sv_available_occupation_skill_points = StringVar()
        sv_available_occupation_skill_points.trace("w", lambda name, index, mode, sv=sv_available_occupation_skill_points: self.update_occupation_skill_points(sv))
        entry_available_occupation_skill_points = Entry(frame_2, textvariable=sv_available_occupation_skill_points, width=5)
        entry_available_occupation_skill_points.grid(row=0, column=1)

        #frame_3
        self.create_skills_labels_and_entries(frame_3)



        #frame_4
        btn_next_window = Button(frame_4, text="Dalej", width=10, command=self.next_window).grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_4, text="Cofnij", width=10, command=self.previous_window).grid(row=0, column=0, pady=20, padx=50, stick=W)
        btn_random = Button(frame_4, text="Random", width=20, command=self.random_button_click).grid(row=1, column=0, columnspan=2, pady=5)



    def create_skills_labels_and_entries(self, frame):
        self.translator = translator.Translator()
        self.label_list = []
        self.entry_dict = {}
        skills_list = self.skill_formater.get_occupation_skills()
        for index, skill in enumerate(skills_list):
            if "lub" in skill:
                or_skills = skill.split(" lub ")
                self.create_dropdown_menu(frame, index, or_skills)
                self.create_entry(frame, index, or_skills[0])

            elif "Dowolna umiejętność" in skill:
                all_skills_enums_list = skills_info.SkillsInfo.get_all_skills_list()
                all_skills_names_pl = [self.translator.get_translation_for_skill(skill) for skill in all_skills_enums_list]
                all_skills_names_pl.sort()
                self.create_dropdown_menu(frame, index, all_skills_names_pl)
                self.create_entry(frame, index, all_skills_names_pl[0])

            else:
                label_skill = Label(frame, text=skill)
                label_skill.grid(row=index, column=0)
                self.label_list.append(label_skill)
                self.create_entry(frame, index, skill)

    def create_dropdown_menu(self, frame, index, skills_names_pl):

        clicked = StringVar()
        clicked.set(skills_names_pl[0])
        dropdown_menu = OptionMenu(frame, clicked, *skills_names_pl)
        dropdown_menu.grid(row=index, column=0)

    def create_entry(self, frame, index, skill):

        min_skill_points = self.skills_into.skills_base_points[self.translator.get_skill_for_translation(skill)]
        if min_skill_points == "0.5 DEX":
            min_skill_points = int(self.calculator.half_value(Data.data[Ability.DEXTERITY]))
        elif min_skill_points == "EDU":
            min_skill_points = int(Data.data[Ability.EDUCATION])
        sv_skill = StringVar()
        sv_skill.trace("w", lambda _, __, ___, sv=sv_skill: Data.save_data(sv, self.translator.get_skill_for_translation(skill)))
        entry_skill_points = Entry(frame, textvariable=sv_skill, width=5)
        entry_skill_points.grid(row=index, column=1)
        entry_skill_points.insert(0, min_skill_points)

    def edit_entry(self):
        pass
    def update_occupation_skill_points(self, sv):
        pass

    def random_button_click(self):
        pass

    def next_window(self):
        self.frame.destroy()

    def previous_window(self):
        self.frame.destroy()
        occupation_select_window.OccupationSelectWindow(self.root)