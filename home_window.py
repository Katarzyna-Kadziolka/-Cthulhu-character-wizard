import random
from tkinter import *
from tkinter import messagebox

import occupation_info_extractor
import random_calculator
import random_skills_points
import skills_info
from Enums.ability import Ability
from Enums.occupation import Occupation
from Enums.skill import Skill
from base_window import BaseWindow
from data import Data
from personal_data_window import PersonalDataWindow
from summary_window import SummaryWindow


class HomeWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)

        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.random_calculator = random_calculator.RandomCalculator()
        self.create_content()

    def create_content(self):
        btn_second_window = Button(self.frame, text="Stwórz postać krok po kroku",command=self.next_window).grid(row=0, column=0, pady=2, sticky=W + E + N + S)
        btn_random_charackter = Button(self.frame, text="Wygeneruj losową postać", command=self.random_whole_character).grid(row=1, column=0, pady=2, stick=W + E + N + S)
        btn_close = Button(self.frame, text="Zamknij", command=self.close_program).grid(row=2, column=0, pady=2, stick=W + E + N + S)

    def close_program(self):
        answer = messagebox.askyesno(title="Zamknij", message="Czy na pewno zamknac?")
        if answer > 0:
            self.root.destroy()
            sys.exit()

    def next_window(self):
        self.frame.destroy()
        PersonalDataWindow(self.root)

    def random_whole_character(self):
        self.save_data("gender", self.random_calculator.get_random_gender())
        self.save_data("first_name", self.random_calculator.get_random_name(Data.data["gender"]))
        self.save_data("last_name", self.random_calculator.get_surname())
        self.save_data("age", int(self.random_calculator.get_age()))

        abilities = self.random_calculator.get_all_random_abilities(Data.data["age"])
        for key, value in abilities.items():
            self.save_data(key, int(value))

        self.save_data(Ability.MOVE_RATE, self.random_calculator.get_move_rate(Data.data[Ability.STRENGTH], Data.data[Ability.DEXTERITY], Data.data[Ability.SIZE], Data.data["age"]))
        self.save_data(Ability.HP, self.random_calculator.get_hp(Data.data[Ability.SIZE], Data.data[Ability.CONDITION]))
        self.save_data(Ability.SANITY, self.random_calculator.get_sanity(Data.data[Ability.POWER]))
        self.save_data(Ability.MAGIC_POINTS, self.random_calculator.get_magic_points(Data.data[Ability.POWER]))
        self.save_data(Ability.BUILD, self.random_calculator.get_build(Data.data[Ability.STRENGTH], Data.data[Ability.SIZE]))
        self.save_data(Ability.DAMAGE_BONUS, self.random_calculator.get_build(Data.data[Ability.STRENGTH], Data.data[Ability.SIZE]))

        info = occupation_info_extractor.get_infos()
        occupation_names_enum = [i.occupation_enum for i in info]
        occupation = random.choice(occupation_names_enum)
        occupation = Occupation.OCCULTIST
        self.save_data("occupation", occupation)

        info_occupation = [i for i in info if i.occupation_enum == Data.data["occupation"]][0]
        self.save_data("occupation_skill_points", self.random_calculator.get_occupation_skills_points(info_occupation.occupation_skills_points, abilities))
        self.save_data("intelligence_skill_points", self.random_calculator.get_intelligence_skill_points(abilities[Ability.INTELLIGENCE]))

        skills_avaible_for_occupation = info_occupation.skills
        skills_avaible_for_occupation = skills_info.SkillsInfo.extend_skill_list(skills_avaible_for_occupation)
        skills_occupation_dict = {}
        for skill in skills_avaible_for_occupation:
            if skill != []:
                if len(skill) == 47:
                    skill = skills_info.SkillsInfo.get_all_skills_list()
                s = random.choice(skill)

                skills_occupation_dict[s] = skills_info.SkillsInfo.get_minimal_skill_points(s)
        skills_from_occupation_dict = self.random_calculator.get_random_skills_points(Data.data["occupation_skill_points"], skills_occupation_dict, "occupation_skill_points", info_occupation.min_credit_rating, info_occupation.max_credit_rating)
        for skill, value in skills_from_occupation_dict.items():
            skill_min_value = skills_info.SkillsInfo.get_minimal_skill_points(skill)
            if skill == Skill.CREDIT_RATING:
                self.save_data(skill, value)
            if skill_min_value < value:
                self.save_data(skill, value)

        skills_personal_dict = self.random_calculator.random_personal_skills_points(Data.data["intelligence_skill_points"],"intelligence_skill_points")
        for skill, value in skills_personal_dict.items():
            self.save_data(skill, value)

        self.frame.destroy()
        SummaryWindow(self.root)


    def save_data(self, feature, feature_value):
        Data.data[feature] = feature_value
