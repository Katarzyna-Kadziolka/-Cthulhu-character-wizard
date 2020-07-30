import random
from tkinter import *
import comboboxes_entries_helper
import random_calculator
import skills_info
from data import Data


class RandomSkillsPoints:
    def __init__(self):
        self.helper = comboboxes_entries_helper.ComboboxesEntriesHelper()
        self.calculator = random_calculator.RandomCalculator()

    def reset_skills_points(self, entry_list, entry_base_skill_points, combobox_dict, label_dict, type_base_points):

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

    def random_personal_skills_points(self):
        all_skills_list = skills_info.SkillsInfo.get_all_skills_list()
        skills_from_data = [key for key, value in Data.data.items()]
        all_skills_list = [skill for skill in all_skills_list if skill not in skills_from_data]
        random_number_of_skills = random.randint(3, 5)
        skills_list = []
        skills_dict = {}
        for n in range(1, random_number_of_skills):
            skill_enum = random.choice(all_skills_list)
            skills_list.append(skill_enum)
            all_skills_list.remove(skill_enum)
        for skill_enum in skills_list:
            skill_min_value = self.helper.get_min_skill_points(skill_enum, "intelligence_skill_points")
            skills_dict[skill_enum] = skill_min_value
        skills_dict = self.calculator.get_random_skills_points(int(Data["intelligence_skill_points"]), skills_dict)

