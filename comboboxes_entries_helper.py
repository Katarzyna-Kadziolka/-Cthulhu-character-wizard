from enum import Enum
from tkinter import *
from tkinter.ttk import Combobox

import skills_info
import translator
from data import Data


class ComboboxesEntriesHelper:

    def __init__(self):
        self.combobox_and_removed_skills = []
        self.skills_info = skills_info.SkillsInfo()
        self.translator = translator.Translator()


    def check_personal_skill_points(self, points_entry, skill_points, entry_list):
        points_entry.config(state="normal")
        if skill_points == '':
            return

        elif int(skill_points) < 0:
            entries_values_list = []
            for entry in entry_list:
                entries_values_list.append(int(entry.get()))
            max_value = 0
            for value in entries_values_list:
                if value > max_value:
                    max_value = value
            entries_with_the_biggest_value = [entry for entry in entry_list if int(entry.get()) == max_value]
            entry_value = int(entries_with_the_biggest_value[0].get())
            entries_with_the_biggest_value[0].delete(0, END)
            entries_with_the_biggest_value[0].insert(0, entry_value + int(skill_points))
            points_entry.delete(0, END)
            points_entry.insert(0, "0")

            for entry in entry_list:
                entry.configure(state="disabled")
            points_entry.config(state="disabled")

        elif int(skill_points) == 0:
            for entry in entry_list:
                entry.configure(state="disabled")
            points_entry.config(state="disabled")

        elif int(skill_points) > 0:
            points_entry.config(state="normal")
            for entry in entry_list:
                entry.configure(state="normal")

        points_entry.config(state="disabled")

        return points_entry


    def update_any_skill_list(self, skill, index, combobox_dict):

        for dictionary in self.combobox_and_removed_skills:
            if dictionary["combobox_index"] == index:
                values = list(dictionary["combobox"]['values'])
                if not dictionary["removed_skill"] in values:
                    values.append(dictionary["removed_skill"])
                    dictionary["combobox"]['values'] = values

        for key, combobox in combobox_dict.items():
            if key == index:
                continue
            skill_names_pl = list(combobox['values'])

            try:
                skill_names_pl.remove(skill)
                self.combobox_and_removed_skills.append({
                    "combobox_index": index,
                    "combobox": combobox,
                    "removed_skill": skill
                })
            except:
                pass
            combobox['values'] = skill_names_pl

        return combobox_dict

    def on_entry_changed(self, sv, index, base_points_entry, entry_list, combobox_dict, label_dict, type_base_points):
        skill = ""
        if index in combobox_dict:
            skill = combobox_dict[index].get()
        elif index in label_dict:
            skill = label_dict[index].cget("text")
        else:
            return
        self.check_skill_points(sv, skill, type_base_points)
        if len(sv.get()) < 2:
            return

        self.update_base_skill_points(base_points_entry, entry_list, combobox_dict, label_dict, type_base_points)


    def save_data(self, entry_list, combobox_dict, label_dict):
        for index, entry in enumerate(entry_list):
            skill = ""
            if index in combobox_dict:
                skill = combobox_dict[index].get()
            elif index in label_dict:
                skill = label_dict[index].cget("text")
            else:
                return
            skill_enum = self.translator.get_skill_for_translation(skill)
            Data.save_data(entry_list[index], skill_enum)


    def check_skill_points(self, sv, skill, type_base_points):
        if sv.get() == "":
            return
        skill_enum = self.translator.get_skill_for_translation(skill)
        min_skill_points = self.get_min_skill_points(skill_enum, type_base_points)
        try:
            int(sv.get())
        except ValueError:
            sv.set(f"{min_skill_points:02d}")
            return

        if len(sv.get()) < 2:
            return

        if int(sv.get()) < min_skill_points:
            sv.set(f"{min_skill_points:02d}")

        elif int(sv.get()) > 99:
            sv.set("99")

        return sv

    def update_base_skill_points(self, base_points_entry, entry_list, combobox_dict, label_dict, type_points):
        base_points_entry.config(state="normal")
        base_points_entry.delete(0, END)
        base_points_entry.insert(0, Data.data[type_points])
        base_points_entry.config(state="disabled")
        for index, entry in enumerate(entry_list):
            if index in label_dict:
                skill_name_pl = label_dict[index].cget("text")
                self.update_base_skill_points_for_skill(skill_name_pl, entry, base_points_entry, type_points)

            elif index in combobox_dict:
                skill_name_pl = combobox_dict[index].get()
                self.update_base_skill_points_for_skill(skill_name_pl, entry, base_points_entry, type_points)

            else:
                raise ValueError(f"Index nr {index} not found")

    def update_base_skill_points_for_skill(self, skill_name_pl, entry, entry_base_points, type_base_points):

        skill_enum = self.translator.get_skill_for_translation(skill_name_pl)
        min_skill_points = self.get_min_skill_points(skill_enum, type_base_points)

        current_skill_points = entry.get()
        if current_skill_points == "":
            current_skill_points = 0

        current_skill_points = int(current_skill_points)
        if current_skill_points > int(min_skill_points):
            used_occupation_points = current_skill_points - min_skill_points
            old_occupation_skill_points = int(entry_base_points.get())
            entry_base_points.config(state="normal")
            entry_base_points.delete(0, END)
            entry_base_points.insert(0, old_occupation_skill_points - used_occupation_points)
            entry_base_points.config(state="disabled")

        return entry_base_points

    def get_min_skill_points(self, skill_enum, type_base_points):

        if type_base_points == "intelligence_skill_points":
            try:
                min_skill_points = Data.data[skill_enum]
            except:
                min_skill_points = skills_info.SkillsInfo.get_minimal_skill_points(skill_enum)
        elif type_base_points == "occupation_skill_points":
            min_skill_points = skills_info.SkillsInfo.get_minimal_skill_points(skill_enum)
        else:
            raise ValueError(f"Type {type_base_points} of points  is incorrect")

        return min_skill_points


    def get_skill_enum_from_label_or_combobox(self, index, combobox_dict, label_dict):
        skill = ""
        if index in combobox_dict:
            skill = combobox_dict[index].get()
        elif index in label_dict:
            skill = label_dict[index].cget("text")
        else:
            return
        skill_enum = self.translator.get_skill_for_translation(skill)

        return skill_enum

    def update_combobox(self, sv, index, combobox_dict, type_base_points, entry_list):
        self.update_entry_with_current_value_of_combobox(index, combobox_dict, type_base_points, entry_list)
        self.update_any_skill_list(sv.get(), index, combobox_dict)

    def update_entry_with_current_value_of_combobox(self, index, combobox_dict, type_base_points, entry_list):
        skill_pl = combobox_dict[index].get()
        enum_skill = self.translator.get_skill_for_translation(skill_pl)
        skill_min_points = self.get_min_skill_points(enum_skill, type_base_points)
        entry_list[index].delete(0, END)
        entry_list[index].insert(0, f"{skill_min_points:02d}")