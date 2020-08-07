import random
from tkinter import *
import comboboxes_entries_helper
import random_calculator
import skills_info
from Enums.skill import Skill
from data import Data


class RandomSkillsPoints:
    def __init__(self):
        self.helper = comboboxes_entries_helper.ComboboxesEntriesHelper()
        self.calculator = random_calculator.RandomCalculator()

    def reset_skills_points(self, entry_list, entry_base_skill_points, combobox_dict, label_dict, type_base_points, button):
        button.config(state=DISABLED)
        for index, entry in enumerate(entry_list):
            skill_enum = self.helper.get_skill_enum_from_label_or_combobox(index, combobox_dict, label_dict)
            skill_min_points = self.helper.get_min_skill_points(skill_enum, type_base_points)

            entry.config(state="normal")
            entry.delete(0, END)
            entry.insert(0, f"{skill_min_points:02d}")

        entry_base_skill_points.config(state="normal")
        entry_base_skill_points.delete(0, END)
        entry_base_skill_points.insert(0, Data.data[type_base_points])

        if type_base_points == "intelligence_skill_points":
            combobox_dict, entry_list = self.remove_comboboxes(combobox_dict, entry_list)

        return combobox_dict, entry_list

    def remove_comboboxes(self, combobox_dict, entry_list):
        copy_entry_list = entry_list.copy()
        for index, combobox in combobox_dict.copy().items():
            if index != 0:
                combobox.destroy()
                entry = copy_entry_list[index]
                entry.destroy()
                combobox_dict.pop(index)

        entry_list = [entry_list[0]]

        return combobox_dict, entry_list



