from enum import Enum
from tkinter.ttk import Combobox

import comboboxes_entries_helper
import occupation_skills_window
import skills_info
import translator
from base_window import BaseWindow
from tkinter import *
from Enums.skill import Skill
from data import Data
from skills_info import SkillsInfo


class SkillsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.entry_list = []
        self.combobox_dict = {}
        self.label_dict = {}
        self.row_number = 0
        self.translator = translator.Translator()
        self.skills_info = skills_info.SkillsInfo()
        self.helper = comboboxes_entries_helper.ComboboxesEntriesHelper()
        self.create_content()

    def create_content(self):
        self.frame = Label(self.root)
        self.frame.grid(sticky=N+S+E+W)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.frame_1 = Label(self.frame)
        self.frame_2 = Label(self.frame)
        self.frame_3 = Label(self.frame)
        self.frame_4 = Label(self.frame)
        self.frame_1.grid(row=0, column=0)
        self.frame_2.grid(row=1, column=0)
        self.frame_3.grid(row=2, column=0, pady=20)
        self.frame_4.grid(row=3, column=0)

        # frame_1
        label_title = Label(self.frame_1, text="Umiejętności personalne", font=("Helvetica", 16)).grid(row=0, column=0)

        # frame_2
        label_personal_skill_points = Label(self.frame_2, text="Dostępne punkty personalne: ").grid(row=0, column=0)
        personal_skill_points = StringVar()
        self.entry_available_personal_skill_points = Entry(self.frame_2, textvariable=personal_skill_points, width=5)
        self.entry_available_personal_skill_points.grid(row=0, column=1)
        self.entry_available_personal_skill_points.insert(0, Data.data["intelligence_skill_points"])
        personal_skill_points.trace("w", lambda _, __, ___, sv=personal_skill_points: self.helper.check_personal_skill_points(self.entry_available_personal_skill_points, personal_skill_points.get(), self.entry_list))
        self.entry_available_personal_skill_points.config(state="disabled")

        # frame_3
        self.all_skill_list = skills_info.SkillsInfo.get_all_skills_list()
        self.all_skill_list = [self.translator.get_translation_for_skill(skill) for skill in self.all_skill_list]
        self.all_skill_list.sort()

        sv_skill = StringVar()
        entry_for_skill = Entry(self.frame_3, textvariable=sv_skill, width=5)
        entry_for_skill.grid(row=0, column=1, padx=10, sticky=E)
        self.entry_list.append(entry_for_skill)
        combobox_index = self.entry_list.index(entry_for_skill)
        sv_skill.trace("w", lambda _, __, ___, sv=sv_skill: self.helper.on_entry_changed(sv, combobox_index, self.entry_available_personal_skill_points, self.entry_list, self.combobox_dict, self.label_dict, "intelligence_skill_points"))
        entry_for_skill.bind('<FocusOut>', self.helper.check_if_value_is_single_number)

        combobox_clicked = StringVar()
        combobox_clicked.set(self.all_skill_list[0])
        skills_combobox = Combobox(self.frame_3, textvariable=combobox_clicked, width=30)
        skills_combobox['values'] = self.all_skill_list
        skills_combobox.grid(row=0, column=0)
        combobox_clicked.trace("w", lambda _, __, ___, sv=combobox_clicked: self.update_combobox(combobox_clicked,
                                                                                                 combobox_index))
        self.combobox_dict[combobox_index] = skills_combobox

        entry_for_skill.insert(0, self.get_minimal_skill_points(self.entry_list.index(entry_for_skill)))

        # frame_4
        self.add_new_skill_button = Button(self.frame_4, text="+", width=50, command=self.add_new_skill).grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        btn_next_window = Button(self.frame_4, text="Dalej", width=10, command=self.next_window).grid(row=1, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(self.frame_4, text="Cofnij", width=10, command=self.previous_window).grid(row=1, column=0, pady=20, padx=50, stick=W)
        btn_random = Button(self.frame_4, text="Random", width=20, command=self.random_button_click).grid(row=2, column=0, columnspan=2, pady=5)
        btn_reset = Button(self.frame_4, text="Reset", width=20, command=self.reset_skills_points).grid(row=3, column=0, columnspan=2, pady=5)

    def add_new_skill(self):
        self.row_number = self.row_number + 1

        sv_skill = StringVar()
        entry_for_skill = Entry(self.frame_3, textvariable=sv_skill, width=5)
        entry_for_skill.grid(row=self.row_number, column=1, padx=10, sticky=E)
        self.entry_list.append(entry_for_skill)
        combobox_index = self.entry_list.index(entry_for_skill)
        sv_skill.trace("w", lambda _, __, ___, sv=sv_skill: self.helper.on_entry_changed(sv, combobox_index, self.entry_available_personal_skill_points, self.entry_list, self.combobox_dict, self.label_dict, "intelligence_skill_points"))
        entry_for_skill.bind('<FocusOut>', self.helper.check_if_value_is_single_number)

        combobox_clicked = StringVar()
        combobox_clicked.set(self.all_skill_list[0])
        skills_combobox = Combobox(self.frame_3, textvariable=combobox_clicked, width=30)

        comboboxes_values = [combobox_value.get() for index, combobox_value in self.combobox_dict.items()]
        self.all_skill_list = [skill for skill in self.all_skill_list if skill not in comboboxes_values]

        skills_combobox['values'] = self.all_skill_list
        skills_combobox.grid(row=self.row_number, column=0)
        combobox_clicked.trace("w", lambda _, __, ___, sv=combobox_clicked: self.update_combobox(combobox_clicked, combobox_index))
        self.combobox_dict[combobox_index] = skills_combobox

        entry_for_skill.insert(0, self.get_minimal_skill_points(self.entry_list.index(entry_for_skill)))

        self.root.geometry(f"400x{500+self.row_number}")


    def get_minimal_skill_points(self, index):
        enum_skill = self.translator.get_skill_for_translation(self.combobox_dict[index].get())
        try:
            skill_min_points = Data.data[enum_skill]
        except:
            skill_min_points = skills_info.SkillsInfo.skills_base_points[enum_skill]

        return skill_min_points


    def update_combobox(self, sv, index):
        self.update_entry_with_current_value_of_combobox(index)
        self.helper.update_any_skill_list(sv.get(), index, self.combobox_dict)

    def update_entry_with_current_value_of_combobox(self, index):
        skill_min_points = self.get_minimal_skill_points(index)
        self.entry_list[index].delete(0, END)
        self.entry_list[index].insert(0, f"{skill_min_points:02d}")

    def next_window(self):
        pass

    def previous_window(self):
        self.frame.destroy()
        occupation_skills_window.OccupationSkillsWindow(self.root)

    def random_button_click(self):
        pass

    def reset_skills_points(self):
        pass







