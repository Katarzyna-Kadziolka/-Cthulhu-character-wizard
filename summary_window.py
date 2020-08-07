import math
from tkinter import *

import credit_rating_calculator
import random_calculator
import skills_info
import skills_window
import translator
from Enums.ability import Ability
from Enums.skill import Skill
from base_window import BaseWindow
import home_window
from data import Data

class SummaryWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.translator = translator.Translator()
        self.random_calculator = random_calculator.RandomCalculator()
        self.credit_rating_calculator = credit_rating_calculator.CreditRatingCalculator()
        self.creat_content()

    def creat_content(self):
        self.root.geometry("")
        self.frame = Label(self.root)
        self.frame.pack(fill="both", expand=True)

        frame_1 = Label(self.frame)
        frame_2 = Label(self.frame, width=40)
        frame_3 = Label(self.frame)
        self.frame_4 = Label(self.frame)
        frame_5 = Label(self.frame)

        frame_1.grid(row=0, column=0)
        frame_2.grid(row=1, column=0)
        frame_3.grid(row=2, column=0)
        self.frame_4.grid(row=3, column=0)
        frame_5.grid(row=4, column=0)

        # frame_1
        label_title = Label(frame_1, text="Dane Badacza", font=("Helvetica", 16)).grid(row=0, column=0)

        #frame_2
        first_name = Data.data["first_name"]
        last_name = Data.data["last_name"]
        gender = Data.data["gender"]
        if gender == "male":
            gender = "M"
        elif gender == "female":
            gender = "K"
        age = Data.data["age"]
        occupation = self.translator.get_translation_for_skill(Data.data["occupation"])

        label_name = Label(frame_2, text=f"{first_name} {last_name}", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2)
        label_gender = Label(frame_2, text=f"Płeć: {gender}").grid(row=1, column=0, stick=W, padx=15)
        label_age = Label(frame_2, text=f"Wiek: {age}").grid(row=2, column=0, stick=W, padx=15)
        label_occupation = Label(frame_2, text=f"Zawód: {occupation}").grid(row=3, column=0, stick=W, padx=15)

        credit_rating = int(Data.data[Skill.CREDIT_RATING])
        spending_level = self.credit_rating_calculator.get_spending_level(credit_rating)
        cash = self.credit_rating_calculator.get_cash(credit_rating)
        assets = self.credit_rating_calculator.get_assets(credit_rating)

        label_spending_level = Label(frame_2, text=f"Wydatki: {spending_level}$").grid(row=1, column=1, stick=W)
        label_cash = Label(frame_2, text=f"Gotówka: {cash}$").grid(row=2, column=1, stick=W)
        label_assets = Label(frame_2, text=f"Majątek: {assets}$").grid(row=3, column=1, stick=W)

        #frame_3
        strength_points = Data.data[Ability.STRENGTH]
        condition_points = Data.data[Ability.CONDITION]
        size_points = Data.data[Ability.SIZE]
        dexterity_points = Data.data[Ability.DEXTERITY]
        appearance_points = Data.data[Ability.APPEARANCE]
        education_points = Data.data[Ability.EDUCATION]
        intelligence_points = Data.data[Ability.INTELLIGENCE]
        power_points = Data.data[Ability.POWER]

        label_character_traits_title = Label(frame_3, text="Cechy Badacza", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        label_strength = Label(frame_3, text=f"Siła: {strength_points} ({self.random_calculator.half_value(int(strength_points))}/{self.random_calculator.one_fifth(int(strength_points))})").grid(row=1, column=0, stick=W, padx=15)
        label_condition = Label(frame_3, text=f"Kondycja: {condition_points} ({self.random_calculator.half_value(int(condition_points))}/{self.random_calculator.one_fifth(int(condition_points))})").grid(row=2, column=0, stick=W, padx=15)
        label_size = Label(frame_3, text=f"Budowa Ciała: {size_points} ({self.random_calculator.half_value(int(size_points))}/{self.random_calculator.one_fifth(int(size_points))})").grid(row=3, column=0, stick=W, padx=15)
        label_dexterity = Label(frame_3, text=f"Zręczność: {dexterity_points} ({self.random_calculator.half_value(int(dexterity_points))}/{self.random_calculator.one_fifth(int(dexterity_points))})").grid(row=4, column=0, stick=W, padx=15)
        label_appearance = Label(frame_3, text=f"Wygląd: {appearance_points} ({self.random_calculator.half_value(int(appearance_points))}/{self.random_calculator.one_fifth(int(appearance_points))})").grid(row=5, column=0, stick=W, padx=15)
        label_education = Label(frame_3, text=f"Edukacja: {education_points} ({self.random_calculator.half_value(int(education_points))}/{self.random_calculator.one_fifth(int(education_points))})").grid(row=6, column=0, stick=W, padx=15)
        label_intelligence = Label(frame_3, text=f"Inteligencja: {intelligence_points} ({self.random_calculator.half_value(int(intelligence_points))}/{self.random_calculator.one_fifth(int(intelligence_points))})").grid(row=7, column=0, stick=W, padx=15)
        label_power = Label(frame_3, text=f"Moc: {power_points} ({self.random_calculator.half_value(int(power_points))}/{self.random_calculator.one_fifth(int(power_points))})").grid(row=8, column=0, stick=W, padx=15)

        move_rate_points = Data.data[Ability.MOVE_RATE]
        hp_points = Data.data[Ability.HP]
        luck_points = Data.data[Ability.LUCK]
        magic_points = Data.data[Ability.MAGIC_POINTS]
        damage_bonus_points = Data.data[Ability.DAMAGE_BONUS]
        build_points = Data.data[Ability.BUILD]
        sanity_points = Data.data[Ability.SANITY]
        try:
            cthulhu_mythos = Data.data[Skill.CTHULHU_MYTHOS]
            sanity_points = self.random_calculator.get_sanity_corrected_by_mythos(sanity_points, cthulhu_mythos)
        except:
            pass

        label_move_rate = Label(frame_3, text=f"Szybkość: {move_rate_points}").grid(row=1, column=1, stick=W)
        label_hp = Label(frame_3, text=f"Wytrzymałość: {hp_points}").grid(row=2, column=1, stick=W)
        label_sanity = Label(frame_3, text=f"Poczytalność: {sanity_points}").grid(row=3, column=1, stick=W)
        label_luck = Label(frame_3, text=f"Szczęście: {luck_points}").grid(row=4, column=1, stick=W)
        label_magic_points = Label(frame_3, text=f"Punkty Magii: {magic_points}").grid(row=5, column=1, stick=W)
        label_damage_bonus = Label(frame_3, text=f"Modyfikator Obrażeń: {damage_bonus_points}").grid(row=6, column=1, stick=W)
        label_build = Label(frame_3, text=f"Postura: {build_points}").grid(row=7, column=1, stick=W)

        #frame_4
        label_character_traits_title = Label(self.frame_4, text="Umiejętności Badacza", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        try:
            native_language_points = Data.data[Skill.OWN_LANGUAGE]
        except:
            native_language_points = Data.data[Ability.EDUCATION]

        try:
            dodge_points = Data.data[Skill.DODGE]
        except:
            dodge_points = self.random_calculator.half_value(int(Data.data[Ability.DEXTERITY]))

        label_native_language = Label(self.frame_4, text=f"Język Ojczysty: {native_language_points} ({self.random_calculator.half_value(int(native_language_points))}/{self.random_calculator.one_fifth(int(native_language_points))})").grid(row=1, column=0, stick=W, padx=15)
        label_dodge = Label(self.frame_4, text=f"Unik: {dodge_points} ({self.random_calculator.half_value(int(dodge_points))}/{self.random_calculator.one_fifth(int(dodge_points))})").grid(row=1, column=1, stick=W)
        self.create_labels()

        #frame_5
        btn_next_window = Button(frame_5, text="Zakończ", width=40, command=self.next_window).grid(row=1, column=1, pady=20, padx=50)


    def create_labels(self):
        skills_from_data = [key for key, value in Data.data.items() if isinstance(key, enum.Enum) and type(key) != Ability and key != Skill.OWN_LANGUAGE and key != Skill.DODGE]
        half_skill_number = math.ceil(len(skills_from_data)/2)
        skills_dict = {}
        row_number = 2
        for skill in skills_from_data:
            skills_dict[skill] = Data.data[skill]
        for skill_enum, skill_points in skills_dict.items():
            skill_pl = self.translator.get_translation_for_skill(skill_enum)
            skill_label = Label(self.frame_4, text=f"{skill_pl}: {skill_points} ({self.random_calculator.half_value(int(skill_points))}/{self.random_calculator.one_fifth(int(skill_points))})")
            if row_number - 1 <= half_skill_number:
                skill_label.grid(row=row_number, column=0, stick=W, padx=15)
            else:
                skill_label.grid(row=row_number-half_skill_number, column=1, stick=W)
            row_number += 1

    def next_window(self):
        Data.data.clear()
        self.frame.destroy()
        self.root.geometry("400x500")
        home_window.HomeWindow(self.root)



