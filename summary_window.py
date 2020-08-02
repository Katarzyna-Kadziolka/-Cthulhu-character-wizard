from tkinter import *

import random_calculator
import skills_info
import translator
from Enums.ability import Ability
from base_window import BaseWindow
from data import Data

class SummaryWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.translator = translator.Translator()
        self.random_calculator = random_calculator.RandomCalculator()
        self.creat_content()

    def creat_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)

        frame_1 = Label(self.frame)
        frame_2 = Label(self.frame)
        frame_3 = Label(self.frame)
        frame_4 = Label(self.frame)
        frame_5 = Label(self.frame)
        frame_6 = Label(self.frame)

        frame_1.grid(row=0, column=0)
        frame_2.grid(row=1, column=0)
        frame_3.grid(row=2, column=0)
        frame_4.grid(row=3, column=0)
        frame_5.grid(row=4, column=0)
        frame_6.grid(row=5, column=0)

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

        label_name = Label(frame_2, text=f"Imię i Nazwisko: {first_name} {last_name}").grid(row=0, column=0)
        label_gender = Label(frame_2, text=f"Płeć: {gender}").grid(row=1, column=0)
        label_age = Label(frame_2, text=f"Wiek: {age}").grid(row=2, column=0)
        label_occupation = Label(frame_2, text=f"Zawód: {occupation}").grid(row=3, column=0)

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
        sanity_points = Data.data[Ability.SANITY]
        luck_points = Data.data[Ability.LUCK]
        magic_points = Data.data[Ability.MAGIC_POINTS]
        damage_bonus_points = Data.data[Ability.DAMAGE_BONUS]
        build_points = Data.data[Ability.BUILD]

        label_move_rate = Label(frame_3, text=f"Szybkość: {move_rate_points}").grid(row=1, column=1, stick=W)
        label_hp = Label(frame_3, text=f"Wytrzymałość: {hp_points}").grid(row=2, column=1, stick=W)
        #TODO sanity zależy od mitów cthulhu
        label_sanity = Label(frame_3, text=f"Poczytalność: {sanity_points}").grid(row=3, column=1, stick=W)
        label_luck = Label(frame_3, text=f"Szczęście: {luck_points}").grid(row=4, column=1, stick=W)
        label_magic_points = Label(frame_3, text=f"Punkty Magii: {magic_points}").grid(row=5, column=1, stick=W)
        label_damage_bonus = Label(frame_3, text=f"Modyfikator Obrażeń: {damage_bonus_points}").grid(row=6, column=1, stick=W)
        label_build = Label(frame_3, text=f"Postura: {build_points}").grid(row=7, column=1, stick=W)

        #frame_4
        label_character_traits_title = Label(frame_4, text="Umiejętności Badacza", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)
        all_skills_list = skills_info.SkillsInfo.get_all_skills_list()
        skills_from_data = [key for key, value in Data.data.items() if isinstance(key, enum.Enum)]