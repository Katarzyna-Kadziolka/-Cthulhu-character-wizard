from tkinter import *
from tkinter import messagebox
import sqlite3
import math
import random
from abilities_calculator import AbilitiesCalculator
from ability import Ability
from database import Database

root = Tk()
root.title("Kreator Badaczy Tajemnic")
root.geometry("400x400")

data = {}
calculator = AbilitiesCalculator()
database = Database()

def update_ability(sv, e_half, e_one_fifth, name):
    if sv.get() != "":
        e_half.delete(0, END)
        e_one_fifth.delete(0, END)
        e_half.insert(0, calculator.half_value(int(sv.get())))
        e_one_fifth.insert(0, calculator.one_fifth(int(sv.get())))
        save_data(sv, name)

def close_program():
    sExit = messagebox.askyesno(title="Zamknij", message="Czy na pewno zamknac?")
    if sExit > 0:
        root.destroy()
        return

def clean_frame(frame_name, num):
    frame_name.destroy()
    to_window(num)

def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)

def next(event, frame_name, num):
    clean_frame(frame_name, num)

def to_window(window_number):
    if window_number == 1:
        first_window()
    elif window_number == 2:
        second_window()
    elif window_number == 3:
        third_window()
    elif window_number == 4:
        print(data)
        fourth_window()

def save_data(sv, name):
    try:
        data[name] = int(sv.get())
    except ValueError:
        data[name] = sv.get()

def random_button_click(entry_abilities):
    x = calculator.get_all_random_abilities(data['age'])

    data.update(x)
    for key, value in entry_abilities.items():
        set_text(value, data[key])



def first_window():

    frame = Label(root)
    frame.place(relx=0.5, rely=0.4, anchor=CENTER)

    btn_second_window = Button(frame, text="Stwórz postać krok po kroku", command=lambda: clean_frame(frame, 2)).grid(row=0, column=0, pady=2, sticky=W + E + N + S)
    btn_random_charackter = Button(frame, text="Wygeneruj losową postać", command=None).grid(row=1, column=0, pady=2, stick=W + E + N + S)
    btn_close = Button(frame, text="Zamknij", command=close_program).grid(row=2, column=0, pady=2, stick=W + E + N + S)


def random_personal_data():
    pass

def second_window():

    frame_2 = Label(root)
    frame_2.place(relx=0.5, rely=0.4, anchor=CENTER)

    sv_f_name = StringVar()
    sv_f_name.trace("w", lambda name, index, mode, sv=sv_f_name: save_data(sv, "first_name"))
    sv_l_name = StringVar()
    sv_l_name.trace("w", lambda name, index, mode, sv=sv_l_name: save_data(sv, "last_name"))
    sv_age = StringVar()
    sv_age.trace("w", lambda name, index, mode, sv=sv_age: save_data(sv, "age"))

    label_f_name = Label(frame_2, text="Imię:").grid(row=0, column=0, stick=E)
    label_l_name = Label(frame_2, text="Nazwisko:").grid(row=1, column=0, stick=E)
    label_age = Label(frame_2, text="Wiek:").grid(row=2, column=0, stick=E)
    label_sex = Label(frame_2, text="Płeć:").grid(row=3, column=0, stick=E)

    e_f_name = Entry(frame_2, textvariable=sv_f_name)
    e_l_name = Entry(frame_2, textvariable=sv_l_name)
    e_age = Entry(frame_2, textvariable=sv_age)

    e_f_name.grid(row=0, column=1,  padx=10)
    e_l_name.grid(row=1, column=1, padx=10)
    e_age.grid(row=2, column=1, padx=10)

    r = StringVar()
    radio = Radiobutton(frame_2, text="♂", variable=r, value="male").grid(row=3, column=1, sticky=W)
    radio = Radiobutton(frame_2, text="♀", variable=r, value="female").grid(row=3, column=2, sticky=W)

    btn_third_window = Button(frame_2, text="Dalej", width=10, command=lambda: clean_frame(frame_2, 3)).grid(row=4, column=1, pady=20, stick=E)
    btn_back = Button(frame_2, text="Cofnij", width=10, command=lambda: clean_frame(frame_2, 1)).grid(row=4, column=0, pady=20, stick=W)
    btn_random_names = Button(frame_2, text="Random", command=lambda: random_personal_data()).grid(row=5, column=0, columnspan=3, pady=5, stick=W + E + N + S)

# TODO ogarnij to radio przestrzennie


def third_window():

    frame_3 = Label(root)
    frame_3_0 = Label(frame_3)
    frame_3_1 = Label(frame_3)
    frame_3_2 = Label(frame_3)
    frame_3_3 = Label(frame_3)
    frame_3_4 = Label(frame_3)

    frame_3.place(relx=0.5, rely=0.4, anchor=CENTER)
    frame_3_0.grid(row=0, column=0, columnspan=2)
    frame_3_1.grid(row=1, column=0, padx=10)
    frame_3_2.grid(row=1, column=1)
    frame_3_3.grid(row=2, column=0, columnspan=2)
    frame_3_4.grid(row=3, column=0, columnspan=2)

    sv_strenght = StringVar()
    sv_strenght.trace("w", lambda name, index, mode, sv=sv_strenght: update_ability(sv, e_half_strength, e_one_fifth_strength, Ability.STRENGTH))
    sv_condition = StringVar()
    sv_condition.trace("w", lambda name, index, mode, sv=sv_condition: update_ability(sv, e_half_condition, e_one_fifth_condition, Ability.STRENGTH))
    sv_size = StringVar()
    sv_size.trace("w", lambda name, index, mode, sv=sv_size: update_ability(sv, e_half_size, e_one_fifth_size, Ability.SIZE))
    sv_dexterity = StringVar()
    sv_dexterity.trace("w", lambda name, index, mode, sv=sv_dexterity: update_ability(sv, e_half_dexterity, e_one_fifth_dexterity, Ability.DEXTERITY))
    sv_appearance = StringVar()
    sv_appearance.trace("w", lambda name, index, mode, sv=sv_appearance: update_ability(sv, e_half_appearance, e_one_fifth_appearance, Ability.APPEARANCE))
    sv_education = StringVar()
    sv_education.trace("w", lambda name, index, mode, sv=sv_education: update_ability(sv, e_half_education, e_one_fifth_education, Ability.EDUCATION))
    sv_intelligence = StringVar()
    sv_intelligence.trace("w", lambda name, index, mode, sv=sv_intelligence: update_ability(sv, e_half_intelligence, e_one_fifth_intelligence, Ability.INTELLIGENCE))
    sv_power = StringVar()
    sv_power.trace("w", lambda name, index, mode, sv=sv_power: update_ability(sv, e_half_power, e_one_fifth_power, Ability.POWER))
    sv_luck = StringVar()
    sv_luck.trace("w", lambda name, index, mode, sv=sv_luck: update_ability(sv, e_half_luck, e_one_fifth_luck, Ability.LUCK))

    #frame_3_0
    l_instruction = Label(frame_3_0, text="Rzut 3K6 pomnożony razy 5", font=("Helvetica", 11)).grid(row=0, column=0, pady=10)

    #frame_3_1
    l_strength = Label(frame_3_1, text="Siła:").grid(row=0, column=0, stick=E, padx=4)
    l_condition = Label(frame_3_1, text="Kondycja:").grid(row=1, column=0, stick=E, padx=4)
    l_dexterity = Label(frame_3_1, text="Zręczność:").grid(row=2, column=0, stick=E, padx=4)

    e_strength = Entry(frame_3_1, textvariable=sv_strenght, width=5, validate="key")
    e_condition = Entry(frame_3_1, textvariable=sv_condition, width=5)
    e_dexterity = Entry(frame_3_1, textvariable=sv_dexterity, width=5)

    e_strength.grid(row=0, column=1)
    e_condition.grid(row=1, column=1)
    e_dexterity.grid(row=2, column=1)

    e_half_strength = Entry(frame_3_1, width=4)
    e_half_condition = Entry(frame_3_1, width=4)
    e_half_dexterity = Entry(frame_3_1, width=4)

    e_half_strength.grid(row=0, column=2)
    e_half_condition.grid(row=1, column=2)
    e_half_dexterity.grid(row=2, column=2)

    e_one_fifth_strength = Entry(frame_3_1, width=4)
    e_one_fifth_condition = Entry(frame_3_1, width=4)
    e_one_fifth_dexterity = Entry(frame_3_1, width=4)

    e_one_fifth_strength.grid(row=0, column=3)
    e_one_fifth_condition.grid(row=1, column=3)
    e_one_fifth_dexterity.grid(row=2, column=3)

    #frame_3_2
    l_appearance = Label(frame_3_2, text="Wygląd:").grid(row=0, column=0, stick=E, padx=4)
    l_power = Label(frame_3_2, text="Moc:").grid(row=1, column=0, stick=E, padx=4)

    e_appearance = Entry(frame_3_2, textvariable=sv_appearance, width=5)
    e_power = Entry(frame_3_2, textvariable=sv_power, width=5)

    e_appearance.grid(row=0, column=1)
    e_power.grid(row=1, column=1)

    e_half_appearance = Entry(frame_3_2, width=4)
    e_half_power = Entry(frame_3_2, width=4)

    e_half_appearance.grid(row=0, column=2)
    e_half_power .grid(row=1, column=2)

    e_one_fifth_appearance = Entry(frame_3_2, width=4)
    e_one_fifth_power = Entry(frame_3_2, width=4)

    e_one_fifth_appearance.grid(row=0, column=3)
    e_one_fifth_power.grid(row=1, column=3)


    #frame_3_3
    l_introduction = Label(frame_3_3, text="Rzut 2K6 + 6 pomnożony razy 5", font=("Helvetica", 11)).grid(row=0, column=0, columnspan=8, pady=20)
    l_size = Label(frame_3_3, text="Budowa ciała:").grid(row=1, column=0, stick=E, padx=4)
    l_intelligence = Label(frame_3_3, text="Inteligencja:").grid(row=2, column=0, stick=E, padx=4)
    l_education = Label(frame_3_3, text="Wykształcenie:").grid(row=1, column=4, stick=E, padx=4)
    l_luck = Label(frame_3_3, text="Szczęście:").grid(row=2, column=4, stick=E, padx=4)

    e_size = Entry(frame_3_3, textvariable=sv_size, width=5)
    e_intelligence = Entry(frame_3_3, textvariable=sv_intelligence, width=5)
    e_education = Entry(frame_3_3, textvariable=sv_education, width=5)
    e_luck = Entry(frame_3_3, textvariable=sv_luck, width=5)

    e_luck.bind('<Return>', lambda event: next(event, frame_3, 4))

    e_size.grid(row=1, column=1)
    e_intelligence.grid(row=2, column=1)
    e_education.grid(row=1, column=5)
    e_luck.grid(row=2, column=5)

    e_half_size = Entry(frame_3_3, width=4)
    e_half_intelligence = Entry(frame_3_3, width=4)
    e_half_education = Entry(frame_3_3, width=4)
    e_half_luck = Entry(frame_3_3, width=4)

    e_half_size.grid(row=1, column=2)
    e_half_intelligence.grid(row=2, column=2)
    e_half_education.grid(row=1, column=6)
    e_half_luck.grid(row=2, column=6)

    e_one_fifth_size = Entry(frame_3_3, width=4)
    e_one_fifth_intelligence = Entry(frame_3_3, width=4)
    e_one_fifth_education = Entry(frame_3_3, width=4)
    e_one_fifth_luck = Entry(frame_3_3, width=4)

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

    #frame_3_4
    btn_fourth_window = Button(frame_3_4, text="Dalej", width=10, command=lambda: clean_frame(frame_3, 4)).grid(row=0, column=1, pady=20, padx=50, stick=E)
    btn_back_window_2 = Button(frame_3_4, text="Cofnij", width=10, command=lambda: clean_frame(frame_3, 2)).grid(row=0, column=0, pady=20, padx=50, stick=W)
    btn_random_values_window_3 = Button(frame_3_4, text="Random", width=20, command=lambda: random_button_click(entry_abilities)).grid(row=1, column=0, columnspan=2, pady=5)


def fourth_window():

    return


first_window()


root.mainloop()