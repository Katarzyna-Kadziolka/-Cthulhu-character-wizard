from tkinter import *
from tkinter.ttk import Combobox
import operator
import occupation_select_window
import random_calculator
import skill_formater
import skills_info
import translator
from Enums.ability import Ability
from Enums.art_craft import ArtCraft
from Enums.fighting import Fighting
from Enums.firearms import Firearm
from Enums.language import Language
from Enums.pilot import Pilot
from Enums.science import Science
from Enums.survival import Survival
from base_window import BaseWindow
from data import Data


class OccupationSkillsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.entry_list = []
        self.combobox_and_removed_skills = []
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
        occupation_skill_points = StringVar()
        self.entry_available_occupation_skill_points = Entry(frame_2, textvariable=occupation_skill_points, width=5)
        self.entry_available_occupation_skill_points.grid(row=0, column=1)
        self.entry_available_occupation_skill_points.insert(0, Data.data["occupation_skill_points"])
        occupation_skill_points.trace("w", lambda _, __, ___, sv=occupation_skill_points: self.check_occupation_skill_points(occupation_skill_points.get()))
        #frame_3
        self.create_skills_labels_and_entries(frame_3)



        #frame_4
        btn_next_window = Button(frame_4, text="Dalej", width=10, command=self.next_window).grid(row=0, column=1, pady=20, padx=50, stick=E)
        btn_previous_window = Button(frame_4, text="Cofnij", width=10, command=self.previous_window).grid(row=0, column=0, pady=20, padx=50, stick=W)
        btn_random = Button(frame_4, text="Random", width=20, command=self.random_button_click).grid(row=1, column=0, columnspan=2, pady=5)


    def check_occupation_skill_points(self, occupation_skill_points):
        if occupation_skill_points == '':
            pass

        elif int(occupation_skill_points) < 0:
            entry_and_value_list = []
            for entry in self.entry_list:
                entry_and_value_dict = {}
                entry_and_value_dict ["entry"] = entry
                entry_and_value_dict ["value"] = entry.get()
                entry_and_value_list.append(entry_and_value_dict)
            max_value = 0
            for dictonary in entry_and_value_list:
                if int(dictonary["value"]) > max_value:
                    max_value = int(dictonary["value"])
            entries_with_the_biggest_value = [entry for entry in self.entry_list if int(entry.get()) == max_value]
            entry_value = int(entries_with_the_biggest_value[0].get())
            entries_with_the_biggest_value[0].delete(0, END)
            entries_with_the_biggest_value[0].insert(0, entry_value + int(occupation_skill_points))
            self.entry_available_occupation_skill_points.delete(0, END)
            self.entry_available_occupation_skill_points.insert(0, "0")

            for entry in self.entry_list:
                entry.configure(state="disabled")
            self.entry_available_occupation_skill_points.config(state="disabled")


        elif int(occupation_skill_points) == 0:
            for entry in self.entry_list:
                entry.configure(state="disabled")
            self.entry_available_occupation_skill_points.config(state="disabled")


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
                entry = self.create_entry(frame, index, or_skills[0])
                self.entry_list.append(entry)
                self.create_combobox(frame, index, or_skills)

            elif "Dowolna umiejętność" in skill:
                all_skills_enums_list = skills_info.SkillsInfo.get_all_skills_list()
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

    def update_any_skill_list(self, skill, index):
        for dictionary in self.combobox_and_removed_skills:
            if dictionary["combobox_index"] == index:
                values = list(dictionary["combobox"]['values'])
                if not dictionary["removed_skill"] in values:
                    values.append(dictionary["removed_skill"])
                    dictionary["combobox"]['values'] = values

        for key, combobox in self.combobox_dict.items():
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

    def clicked_methods(self, clicked, index):
        self.update_entry_with_current_value_of_combobox(clicked, index)
        self.update_any_skill_list(clicked.get(), index)

    def create_combobox(self, frame, index, skills_names_pl):
        clicked = StringVar()
        clicked.set(skills_names_pl[0])
        combobox = Combobox(frame, textvariable=clicked, width=30)
        combobox['values'] = skills_names_pl
        combobox.grid(row=index, column=0)
        self.combobox_dict[index] = combobox
        clicked.trace("w", lambda _, __, ___, sv=clicked: self.clicked_methods(clicked, index))
        return combobox

    def on_entry_changed(self, sv, skill):
        Data.save_data(sv, self.translator.get_skill_for_translation(skill))
        self.update_occupation_skill_points()

    def create_entry(self, frame, index, skill):

        min_skill_points = self.skills_into.skills_base_points[self.translator.get_skill_for_translation(skill)]
        if min_skill_points == "0.5 DEX":
            min_skill_points = int(self.calculator.half_value(Data.data[Ability.DEXTERITY]))
        elif min_skill_points == "EDU":
            min_skill_points = int(Data.data[Ability.EDUCATION])
        sv_skill = StringVar()
        sv_skill.trace("w", lambda _, __, ___, sv=sv_skill: self.on_entry_changed(sv, skill))
        entry_skill_points = Entry(frame, textvariable=sv_skill, width=5)
        entry_skill_points.grid(row=index, column=1, padx=5)
        entry_skill_points.insert(0, min_skill_points)
        return entry_skill_points

    def update_entry_with_current_value_of_combobox(self, clicked, index):
        enum_skill = self.translator.get_skill_for_translation(clicked.get())
        skill_min_points = skills_info.SkillsInfo.skills_base_points[enum_skill]
        self.entry_list[index].delete(0, END)
        self.entry_list[index].insert(0, skill_min_points)

    def update_occupation_skill_points_for_skill(self, skill_name_pl, entry):

        skill_enum = self.translator.get_skill_for_translation(skill_name_pl)
        min_skill_points = skills_info.SkillsInfo.get_minimal_skill_points(skill_enum)
        current_skill_points = entry.get()
        if current_skill_points == "":
            return None

        current_skill_points = int(current_skill_points)
        if current_skill_points > int(min_skill_points):
            used_occupation_points = current_skill_points - min_skill_points
            old_occupation_skill_points = int(self.entry_available_occupation_skill_points.get())
            self.entry_available_occupation_skill_points.delete(0, END)
            self.entry_available_occupation_skill_points.insert(0, old_occupation_skill_points - used_occupation_points)

    def update_occupation_skill_points(self):
        self.entry_available_occupation_skill_points.delete(0, END)
        self.entry_available_occupation_skill_points.insert(0, Data.data["occupation_skill_points"])
        for index, entry in enumerate(self.entry_list):
            if index in self.label_dict:
                skill_name_pl = self.label_dict[index].cget("text")
                self.update_occupation_skill_points_for_skill(skill_name_pl, entry)

            elif index in self.combobox_dict:
                skill_name_pl = self.combobox_dict[index].get()
                self.update_occupation_skill_points_for_skill(skill_name_pl, entry)


    def random_button_click(self):
        pass

    def next_window(self):
        self.frame.destroy()

    def previous_window(self):
        self.frame.destroy()
        occupation_select_window.OccupationSelectWindow(self.root)