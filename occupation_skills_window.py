import random
from tkinter import *
from tkinter.ttk import Combobox
import operator

import comboboxes_entries_helper
import occupation_select_window
import random_calculator
import random_skills_points
import skill_formater
import skills_info
import skills_window
import translator
from Enums.ability import Ability
from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.occupation import Occupation
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.skill import Skill
from Enums.survival import Survival
from base_window import BaseWindow
from data import Data


class OccupationSkillsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.entry_list = []
        self.combobox_and_removed_skills = []
        self.helper = comboboxes_entries_helper.ComboboxesEntriesHelper()
        self.random_skills_points = random_skills_points.RandomSkillsPoints()
        self.calculator = random_calculator.RandomCalculator()
        self.skills_info = skills_info.SkillsInfo()
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
        occupation_skill_points = StringVar()
        self.entry_available_occupation_skill_points = Entry(frame_2, textvariable=occupation_skill_points, width=5)
        self.entry_available_occupation_skill_points.grid(row=0, column=1)
        self.entry_available_occupation_skill_points.insert(0, Data.data["occupation_skill_points"])
        occupation_skill_points.trace("w", lambda _, __, ___, sv=occupation_skill_points: self.helper.check_personal_skill_points(self.entry_available_occupation_skill_points, occupation_skill_points.get(), self.entry_list))
        self.entry_available_occupation_skill_points.config(state="disabled")

        #frame_3
        self.translator = translator.Translator()
        self.create_skills_labels_and_entries(frame_3)

        #frame_4
        btn_next_window = Button(frame_4, text="Dalej", width=10, command=self.next_window).grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_4, text="Cofnij", width=10, command=self.previous_window).grid(row=0, column=0, pady=20, padx=50, stick=W)
        btn_random = Button(frame_4, text="Random", width=20, command=self.random_button_click).grid(row=1, column=0, columnspan=2, pady=5)
        btn_reset = Button(frame_4, text="Reset", width=20, command=self.reset_skills_points).grid(row=2, column=0, columnspan=2, pady=5)


    def create_combobox_pair_for_enum(self, enum,  index, frame):
        skills = enum.__members__.items()
        skill_pl = [self.translator.get_translation_for_skill(i[1]) for i in skills]
        skill_pl.sort()
        entry = self.create_entry(frame, index, skill_pl[0])
        self.entry_list.append(entry)
        self.create_combobox(frame, index, skill_pl)


    def create_skills_labels_and_entries(self, frame):
        self.translator = translator.Translator()
        self.label_dict = {}

        self.combobox_dict = {}

        skills_list = self.skill_formater.get_occupation_skills()
        for index, skill in enumerate(skills_list):
            if "lub" in skill:
                or_skills = skill.split(" lub ")
                for or_skill in or_skills.copy():
                    or_skill_enum = self.translator.get_skill_for_translation(or_skill)
                    or_skill_enum_string = or_skill_enum.name.title()
                    if or_skill_enum_string == "Other_Language":
                        or_skill_enum_string = "Other Language"
                    if or_skill_enum_string.strip() in skills_info.SkillsInfo.enums_dict.keys():
                        or_skills.remove(or_skill)
                        enum = skills_info.SkillsInfo.enums_dict[or_skill_enum_string.strip()]
                        enum_list = [member[1] for member in enum.__members__.items()]
                        for e in enum_list:
                            or_skills.append(self.translator.get_translation_for_skill(e))
                or_skills.sort()
                entry = self.create_entry(frame, index, or_skills[0])
                self.entry_list.append(entry)
                self.create_combobox(frame, index, or_skills)

            elif "Dowolna umiejętność" in skill:
                all_skills_enums_list = skills_info.SkillsInfo.get_all_skills_list()
                if Data.data["occupation"] == Occupation.OCCULTIST:
                    all_skills_enums_list.append(Skill.CTHULHU_MYTHOS)
                all_skills_names_pl = [self.translator.get_translation_for_skill(skill) for skill in all_skills_enums_list]
                all_skills_names_pl.sort()
                entry = self.create_entry(frame, index, all_skills_names_pl[0])
                self.entry_list.append(entry)
                self.create_combobox(frame, index, all_skills_names_pl)

            elif skill == "Sztuka/Rzemiosło":
                self.create_combobox_pair_for_enum(ArtCraft, index, frame)

            elif skill == "Język Obcy":
                self.create_combobox_pair_for_enum(Language, index, frame)

            elif skill == "Walka Wręcz":
                self.create_combobox_pair_for_enum(Fighting, index, frame)

            elif skill == "Broń Palna":
                self.create_combobox_pair_for_enum(Firearm, index, frame)

            elif skill == "Nauka":
                self.create_combobox_pair_for_enum(Science, index, frame)

            elif skill == "Pilotowanie":
                self.create_combobox_pair_for_enum(Pilot, index, frame)

            elif skill == "Sztuka Przetrwania":
                self.create_combobox_pair_for_enum(Survival, index, frame)

            else:
                entry = self.create_entry(frame, index, skill)
                self.entry_list.append(entry)
                label_skill = Label(frame, text=skill)
                label_skill.grid(row=index, column=0)
                self.label_dict[index] = label_skill

        self.remove_labels_skills_from_comboboxes()


    def remove_labels_skills_from_comboboxes(self):
        for combobox in self.combobox_dict.values():
            combobox_skills_list = list(combobox["values"])
            for label_skill in self.label_dict.values():
                skill = label_skill.cget("text")
                if skill in combobox_skills_list:
                    combobox_skills_list.remove(skill)
            combobox["values"] = combobox_skills_list

    def create_combobox(self, frame, index, skills_names_pl):
        clicked = StringVar()
        clicked.set(skills_names_pl[0])
        combobox = Combobox(frame, textvariable=clicked, width=30)
        combobox['values'] = skills_names_pl
        combobox.grid(row=index, column=0)
        self.combobox_dict[index] = combobox
        clicked.trace("w", lambda _, __, ___, sv=clicked: self.helper.update_combobox(clicked, index, self.combobox_dict, "occupation_skill_points", self.entry_list))
        return combobox

    def get_minimal_skill_points(self, index):
        if index in self.label_dict:
            enum_skill = self.translator.get_skill_for_translation(self.label_dict[index].cget("text"))
            skill_min_points = skills_info.SkillsInfo.skills_base_points[enum_skill]
        elif index in self.combobox_dict:
            enum_skill = self.translator.get_skill_for_translation(self.combobox_dict[index].get())
            skill_min_points = skills_info.SkillsInfo.skills_base_points[enum_skill]
        else:
            raise ValueError(f"Index {index} don't exist.")

        return skill_min_points

    def check_if_value_is_single_number(self, event):
        try:
            index = self.entry_list.index(event.widget)
        except:
            return
        if len(event.widget.get()) == 0:
            skill_min_points = self.get_minimal_skill_points(index)
            event.widget.delete(0, END)
            event.widget.insert(0, f"{skill_min_points:02d}")

        elif len(event.widget.get()) == 1:
            value = int(event.widget.get())
            event.widget.delete(0, END)
            event.widget.insert(0, f"{value:02d}")


    def create_entry(self, frame, index, skill_pl):
        min_skill_points = self.skills_info.get_minimal_skill_points(self.translator.get_skill_for_translation(skill_pl))
        sv_skill = StringVar()
        sv_skill.trace("w", lambda _, __, ___, sv=sv_skill: self.helper.on_entry_changed(sv, index, self.entry_available_occupation_skill_points, self.entry_list, self.combobox_dict, self.label_dict, "occupation_skill_points"))
        entry_skill_points = Entry(frame, textvariable=sv_skill, width=5)
        entry_skill_points.grid(row=index, column=1, padx=5)
        entry_skill_points.insert(0, f"{min_skill_points:02d}")
        entry_skill_points.bind('<FocusOut>', self.check_if_value_is_single_number)
        return entry_skill_points

    def reset_skills_points(self):
        self.combobox_dict, self.entry_list = self.random_skills_points.reset_skills_points(self.entry_list, self.entry_available_occupation_skill_points, self.combobox_dict, self.label_dict, "occupation_skill_points")

    def set_random_skills_from_comboboxes(self):
        for key in self.combobox_dict:
            combobox = self.combobox_dict[key]
            skill_list = combobox['values']
            skill = random.choice(skill_list)
            combobox.set(skill)

    def random_button_click(self):
        self.set_random_skills_from_comboboxes()
        old_skill_dict = {}
        for key in self.label_dict:
            skill_label = self.label_dict[key]
            skill_enum = self.translator.get_skill_for_translation(skill_label.cget("text"))
            current_points = int(self.entry_list[key].get())
            old_skill_dict[skill_enum] = current_points
        for key in self.combobox_dict:
            skill_combobox = self.combobox_dict[key]
            skill_enum = self.translator.get_skill_for_translation(skill_combobox.get())
            current_points = int(self.entry_list[key].get())
            old_skill_dict[skill_enum] = current_points

        self.entry_available_occupation_skill_points.config(state="normal")
        all_occupation_skills_points = int(self.entry_available_occupation_skill_points.get())
        self.entry_available_occupation_skill_points.config(state="disabled")
        new_skill_dict = self.calculator.get_random_skills_points(all_occupation_skills_points, old_skill_dict.copy())
        labels_text = [self.label_dict[key].cget("text") for key in self.label_dict]
        comboboxes_text = [self.combobox_dict[key].get() for key in self.combobox_dict]
        for key in new_skill_dict:
            skill_pl = self.translator.get_translation_for_skill(key)
            if skill_pl in labels_text:
                skill_label = [skill_label for key, skill_label in self.label_dict.items() if skill_pl == skill_label.cget("text")][0]
                index = [key for key in self.label_dict if self.label_dict[key] == skill_label][0]

            elif skill_pl in comboboxes_text:
                skill_combobox = [skill_combobox for key, skill_combobox in self.combobox_dict.items() if skill_pl == skill_combobox.get()][0]
                index = [key for key in self.combobox_dict if self.combobox_dict[key] == skill_combobox][0]

            else:
                raise ValueError(f"skill {skill_pl} is not used")

            skill_entry = self.entry_list[index]
            self.set_text(skill_entry, new_skill_dict[key])

    def next_window(self):
        self.helper.save_data(self.entry_list, self.combobox_dict, self.label_dict)
        self.frame.destroy()
        skills_window.SkillsWindow(self.root)

    def previous_window(self):
        self.frame.destroy()
        occupation_select_window.OccupationSelectWindow(self.root)