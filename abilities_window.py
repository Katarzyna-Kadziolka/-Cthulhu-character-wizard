from tkinter import *

import personal_data_window
from random_calculator import RandomCalculator
from Enums.ability import Ability
from base_window import BaseWindow
from data import Data
from other_abilities_window import OtherAbilitiesWindow



class AbilitiesWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.entry_list = []
        self.create_content()
        self.calculator = RandomCalculator()

    def create_content(self):
        self.frame = Label(self.root)
        frame_0 = Label(self.frame)
        frame_1 = Label(self.frame)
        frame_2 = Label(self.frame)
        frame_3 = Label(self.frame)
        frame_4 = Label(self.frame)

        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        frame_0.grid(row=0, column=0, columnspan=2)
        frame_1.grid(row=1, column=0, padx=10)
        frame_2.grid(row=1, column=1)
        frame_3.grid(row=2, column=0, columnspan=2)
        frame_4.grid(row=3, column=0, columnspan=2)

        sv_strenght = StringVar()
        sv_strenght.trace("w", lambda name, index, mode, sv=sv_strenght: self.update_ability(sv, e_strength, e_half_strength, e_one_fifth_strength, Ability.STRENGTH))

        sv_condition = StringVar()
        sv_condition.trace("w", lambda name, index, mode, sv=sv_condition: self.update_ability(sv, e_condition, e_half_condition,e_one_fifth_condition, Ability.CONDITION))

        sv_size = StringVar()
        sv_size.trace("w", lambda name, index, mode, sv=sv_size: self.update_ability(sv, e_size, e_half_size, e_one_fifth_size, Ability.SIZE))

        sv_dexterity = StringVar()
        sv_dexterity.trace("w", lambda name, index, mode, sv=sv_dexterity: self.update_ability(sv, e_dexterity, e_half_dexterity, e_one_fifth_dexterity, Ability.DEXTERITY))

        sv_appearance = StringVar()
        sv_appearance.trace("w", lambda name, index, mode, sv=sv_appearance: self.update_ability(sv, e_appearance, e_half_appearance, e_one_fifth_appearance, Ability.APPEARANCE))

        sv_education = StringVar()
        sv_education.trace("w", lambda name, index, mode, sv=sv_education: self.update_ability(sv, e_education, e_half_education, e_one_fifth_education, Ability.EDUCATION))

        sv_intelligence = StringVar()
        sv_intelligence.trace("w", lambda name, index, mode, sv=sv_intelligence: self.update_ability(sv, e_intelligence, e_half_intelligence, e_one_fifth_intelligence, Ability.INTELLIGENCE))

        sv_power = StringVar()
        sv_power.trace("w", lambda name, index, mode, sv=sv_power: self.update_ability(sv, e_power, e_half_power, e_one_fifth_power, Ability.POWER))

        sv_luck = StringVar()
        sv_luck.trace("w", lambda name, index, mode, sv=sv_luck: self.update_ability(sv, e_luck, e_half_luck, e_one_fifth_luck, Ability.LUCK))

        # frame_0
        l_instruction = Label(frame_0, text="Rzut 3K6 pomnożony razy 5", font=("Helvetica", 11)).grid(row=0, column=0, pady=10)

        # frame_1
        l_strength = Label(frame_1, text="Siła:").grid(row=0, column=0, stick=E, padx=4)
        l_condition = Label(frame_1, text="Kondycja:").grid(row=1, column=0, stick=E, padx=4)
        l_dexterity = Label(frame_1, text="Zręczność:").grid(row=2, column=0, stick=E, padx=4)

        e_strength = Entry(frame_1, textvariable=sv_strenght, width=5, validate="key")
        e_condition = Entry(frame_1, textvariable=sv_condition, width=5)
        e_dexterity = Entry(frame_1, textvariable=sv_dexterity, width=5)

        e_strength.grid(row=0, column=1)
        e_condition.grid(row=1, column=1)
        e_dexterity.grid(row=2, column=1)

        self.entry_list.append(e_strength)
        self.entry_list.append(e_condition)
        self.entry_list.append(e_dexterity)

        e_half_strength = Entry(frame_1, width=4, state=DISABLED)
        e_half_condition = Entry(frame_1, width=4, state=DISABLED)
        e_half_dexterity = Entry(frame_1, width=4, state=DISABLED)

        e_half_strength.grid(row=0, column=2)
        e_half_condition.grid(row=1, column=2)
        e_half_dexterity.grid(row=2, column=2)

        e_one_fifth_strength = Entry(frame_1, width=4, state=DISABLED)
        e_one_fifth_condition = Entry(frame_1, width=4, state=DISABLED)
        e_one_fifth_dexterity = Entry(frame_1, width=4, state=DISABLED)

        e_one_fifth_strength.grid(row=0, column=3)
        e_one_fifth_condition.grid(row=1, column=3)
        e_one_fifth_dexterity.grid(row=2, column=3)

        # frame_2
        l_appearance = Label(frame_2, text="Wygląd:").grid(row=0, column=0, stick=E, padx=4)
        l_power = Label(frame_2, text="Moc:").grid(row=1, column=0, stick=E, padx=4)

        e_appearance = Entry(frame_2, textvariable=sv_appearance, width=5)
        e_power = Entry(frame_2, textvariable=sv_power, width=5)

        e_appearance.grid(row=0, column=1)
        e_power.grid(row=1, column=1)

        self.entry_list.append(e_appearance)
        self.entry_list.append(e_power)

        e_half_appearance = Entry(frame_2, width=4, state=DISABLED)
        e_half_power = Entry(frame_2, width=4, state=DISABLED)

        e_half_appearance.grid(row=0, column=2)
        e_half_power.grid(row=1, column=2)

        e_one_fifth_appearance = Entry(frame_2, width=4, state=DISABLED)
        e_one_fifth_power = Entry(frame_2, width=4, state=DISABLED)

        e_one_fifth_appearance.grid(row=0, column=3)
        e_one_fifth_power.grid(row=1, column=3)

        # frame_3
        l_introduction = Label(frame_3, text="Rzut 2K6 + 6 pomnożony razy 5", font=("Helvetica", 11)).grid(row=0, column=0, columnspan=8, pady=20)
        l_size = Label(frame_3, text="Budowa ciała:").grid(row=1, column=0, stick=E, padx=4)
        l_intelligence = Label(frame_3, text="Inteligencja:").grid(row=2, column=0, stick=E, padx=4)
        l_education = Label(frame_3, text="Wykształcenie:").grid(row=1, column=4, stick=E, padx=4)
        l_luck = Label(frame_3, text="Szczęście:").grid(row=2, column=4, stick=E, padx=4)

        e_size = Entry(frame_3, textvariable=sv_size, width=5)
        e_intelligence = Entry(frame_3, textvariable=sv_intelligence, width=5)
        e_education = Entry(frame_3, textvariable=sv_education, width=5)
        e_luck = Entry(frame_3, textvariable=sv_luck, width=5)

        e_size.grid(row=1, column=1)
        e_intelligence.grid(row=2, column=1)
        e_education.grid(row=1, column=5)
        e_luck.grid(row=2, column=5)

        self.entry_list.append(e_size)
        self.entry_list.append(e_intelligence)
        self.entry_list.append(e_education)
        self.entry_list.append(e_luck)


        e_half_size = Entry(frame_3, width=4, state=DISABLED)
        e_half_intelligence = Entry(frame_3, width=4, state=DISABLED)
        e_half_education = Entry(frame_3, width=4, state=DISABLED)
        e_half_luck = Entry(frame_3, width=4, state=DISABLED)

        e_half_size.grid(row=1, column=2)
        e_half_intelligence.grid(row=2, column=2)
        e_half_education.grid(row=1, column=6)
        e_half_luck.grid(row=2, column=6)

        e_one_fifth_size = Entry(frame_3, width=4, state=DISABLED)
        e_one_fifth_intelligence = Entry(frame_3, width=4, state=DISABLED)
        e_one_fifth_education = Entry(frame_3, width=4, state=DISABLED)
        e_one_fifth_luck = Entry(frame_3, width=4, state=DISABLED)

        e_one_fifth_size.grid(row=1, column=3)
        e_one_fifth_intelligence.grid(row=2, column=3)
        e_one_fifth_education.grid(row=1, column=7)
        e_one_fifth_luck.grid(row=2, column=7)

        entry_abilities = {
            Ability.STRENGTH: e_strength,
            Ability.CONDITION: e_condition,
            Ability.SIZE: e_size,
            Ability.DEXTERITY: e_dexterity,
            Ability.APPEARANCE: e_appearance,
            Ability.EDUCATION: e_education,
            Ability.INTELLIGENCE: e_intelligence,
            Ability.POWER: e_power,
            Ability.LUCK: e_luck
        }

        # frame_4
        self.btn_fourth_window = Button(frame_4, text="Dalej", width=10, command=self.next_window, state=DISABLED)
        self.btn_fourth_window.grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_back_window_2 = Button(frame_4, text="Cofnij", width=10, command=self.previous_window).grid(
            row=0, column=0, pady=20, padx=50, stick=W)
        btn_random_values_window_3 = Button(frame_4, text="Random", width=20, command=lambda: self.random_button_click(entry_abilities)).grid(row=1, column=0, columnspan=2, pady=5)

    def random_button_click(self, entry_abilities):
        x = self.calculator.get_all_random_abilities(Data.data['age'])
        Data.data.update(x)
        for key, value in entry_abilities.items():
            self.set_text(value, Data.data[key])
    
    def previous_window(self):
        self.frame.destroy()
        personal_data_window.PersonalDataWindow(self.root)
    
    def next_window(self):
        self.frame.destroy()
        OtherAbilitiesWindow(self.root)

    def update_ability(self, sv, entry, e_half, e_one_fifth, name):
        e_half.config(state=NORMAL)
        e_one_fifth.config(state=NORMAL)

        try:
            int_value = int(sv.get())
            self.set_text(e_half, self.calculator.half_value(int_value))
            self.set_text(e_one_fifth, self.calculator.one_fifth(int_value))
            Data.save_data(sv, name)
        except:
            entry.delete(0, END)

        e_half.config(state=DISABLED)
        e_one_fifth.config(state=DISABLED)

        self.check_fill_entry(self.btn_fourth_window, self.entry_list)



