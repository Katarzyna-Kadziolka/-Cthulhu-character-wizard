from tkinter import *
from tkinter import messagebox
import sqlite3
import math

root = Tk()
root.title("Kreator Badaczy Tajemnic")
root.geometry("400x400")

data = {}

def half_value (num):
    result = math.floor(num/2)
    return result

def one_fifth (num):
    result = math.floor(num/5)
    return result

def callback(event, name, e_half, e_one_fifth):
    e_half.insert(0, half_value(int(name.get())))
    e_one_fifth.insert(0, one_fifth(int(name.get())))

def close_program():
    sExit = messagebox.askyesno(title="Zamknij", message="Czy na pewno zamknac?")
    if sExit > 0:
        root.destroy()
        return

def random(var):
    if var == 1:
        return
    elif var == 2:
        return
    elif var == 3:
        random_K6()

def random_K6():
    return

def to_window(var):
    if var == 0:
        frame_2.destroy()
        first_window()
    elif var == 1:
        frame.destroy()
        second_window()
    elif var == 2:
        data['f_name'] = e_f_name.get()
        data['l_name'] = e_l_name.get()
        data['age'] = e_age.get()
        frame_2.destroy()
        third_window()
    elif var == 3:
        data['strength'] = e_strength.get()
        data['condition'] = e_condition.get()
        data['size'] = e_size.get()
        data['dexterity'] = e_dexterity.get()
        data['appearance'] = e_appearance.get()
        data['education'] = e_education.get()
        data['intelligence'] = e_intelligence.get()
        data['power'] = e_power.get()
        data['luck'] = e_luck.get()

        frame_3.destroy()

        print(data)
        fourth_window()

    elif var == 4:

        frame_4.destroy()


def first_window():
    global frame

    frame = Label(root)
    frame.place(relx=0.5, rely=0.4, anchor=CENTER)

    btn_second_window = Button(frame, text="Stwórz postać krok po kroku", command=lambda: to_window(1))
    btn_random_charackter = Button(frame, text="Wygeneruj losową postać", command=lambda: random(1))
    btn_close = Button(frame, text="Zamknij", command=close_program)

    btn_second_window.grid(row=0, column=0, pady=2, sticky=W + E + N + S)
    btn_random_charackter.grid(row=1, column=0, pady=2, stick=W + E + N + S)
    btn_close.grid(row=2, column=0, pady=2, stick=W + E + N + S)

def second_window():
    global frame_2
    global e_f_name
    global e_l_name
    global e_age

    frame_2 = Label(root)
    frame_2.place(relx=0.5, rely=0.4, anchor=CENTER)

    label_f_name = Label(frame_2, text="Imię:")
    label_l_name = Label(frame_2, text="Nazwisko:")
    label_age = Label(frame_2, text="Wiek:")
    e_f_name = Entry(frame_2)
    e_l_name = Entry(frame_2)
    e_age = Entry(frame_2)
    btn_third_window = Button(frame_2, text="Dalej", width=10, command=lambda: to_window(2))
    btn_back = Button(frame_2, text="Cofnij", width=10, command=lambda: to_window(0))
    btn_random_names = Button(frame_2, text="Random", command=lambda: random(2))

    label_f_name.grid(row=0, column=0, stick=E)
    label_l_name.grid(row=1, column=0, stick=E)
    label_age.grid(row=2, column=0, stick=E)
    e_f_name.grid(row=0, column=1, padx=10)
    e_l_name.grid(row=1, column=1, padx=10)
    e_age.grid(row=2, column=1, padx=10)
    btn_third_window.grid(row=3, column=1, pady=20, stick=E)
    btn_back.grid(row=3, column=0, pady=20, stick=W)
    btn_random_names.grid(row=4, column=0, columnspan=2, pady=5, stick=W+E+N+S)


def third_window():

    global frame_3
    global e_strength
    global e_condition
    global e_size
    global e_dexterity
    global e_appearance
    global e_education
    global e_intelligence
    global e_power
    global e_luck


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

    #frame_3_0
    l_instruction = Label(frame_3_0, text="Rzut 3K6 pomnożony razy 5", font=("Helvetica", 11))
    l_instruction.grid(row=0, column=0, pady=10)

    #frame_3_1
    l_strength = Label(frame_3_1, text="Siła:")
    l_condition = Label(frame_3_1, text="Kondycja:")
    l_size = Label(frame_3_1, text="Budowa ciała:")
    l_dexterity = Label(frame_3_1, text="Zręczność:")

    e_strength = Entry(frame_3_1, width=5)
    e_condition = Entry(frame_3_1, width=5)
    e_size = Entry(frame_3_1, width=5)
    e_dexterity = Entry(frame_3_1, width=5)

    e_strength.bind('<Return>', lambda event:callback(event, e_strength, e_half_strength, e_one_fifth_strength))
    e_condition.bind('<Return>', lambda event:callback(event, e_condition, e_half_condition, e_one_fifth_condition))
    e_size.bind('<Return>', lambda event:callback(event, e_size, e_half_size, e_one_fifth_size))
    e_dexterity.bind('<Return>', lambda event:callback(event, e_dexterity, e_half_dexterity, e_one_fifth_dexterity))

    e_half_strength = Entry(frame_3_1, width=4)
    e_half_condition = Entry(frame_3_1, width=4)
    e_half_size = Entry(frame_3_1, width=4)
    e_half_dexterity = Entry(frame_3_1, width=4)

    e_one_fifth_strength = Entry(frame_3_1, width=4)
    e_one_fifth_condition = Entry(frame_3_1, width=4)
    e_one_fifth_size = Entry(frame_3_1, width=4)
    e_one_fifth_dexterity = Entry(frame_3_1, width=4)

    l_strength.grid(row=0, column=0, stick=E, padx=4)
    l_condition.grid(row=1, column=0, stick=E, padx=4)
    l_size.grid(row=2, column=0, stick=E, padx=4)
    l_dexterity.grid(row=3, column=0, stick=E, padx=4)

    e_strength.grid(row=0, column=1)
    e_condition.grid(row=1, column=1)
    e_size.grid(row=2, column=1)
    e_dexterity.grid(row=3, column=1)

    e_half_strength.grid(row=0, column=2)
    e_half_condition.grid(row=1, column=2)
    e_half_size.grid(row=2, column=2)
    e_half_dexterity.grid(row=3, column=2)

    e_one_fifth_strength.grid(row=0, column=3)
    e_one_fifth_condition.grid(row=1, column=3)
    e_one_fifth_size.grid(row=2, column=3)
    e_one_fifth_dexterity.grid(row=3, column=3)


    #frame_3_2
    l_appearance = Label(frame_3_2, text="Wygląd:")
    l_education = Label(frame_3_2, text="Wykształcenie:")
    l_intelligence = Label(frame_3_2, text="Inteligencja:")
    l_power = Label(frame_3_2, text="Moc:")

    e_appearance = Entry(frame_3_2, width=5)
    e_education = Entry(frame_3_2, width=5)
    e_intelligence = Entry(frame_3_2, width=5)
    e_power = Entry(frame_3_2, width=5)

    e_appearance.bind('<Return>', lambda event:callback(event, e_appearance, e_half_appearance, e_one_fifth_appearance))
    e_education.bind('<Return>', lambda event:callback(event, e_education, e_half_education, e_one_fifth_education))
    e_intelligence.bind('<Return>', lambda event:callback(event, e_intelligence, e_half_intelligence, e_one_fifth_intelligence))
    e_power.bind('<Return>', lambda event:callback(event, e_power, e_half_power, e_one_fifth_power))

    e_half_appearance = Entry(frame_3_2, width=4)
    e_half_education = Entry(frame_3_2, width=4)
    e_half_intelligence = Entry(frame_3_2, width=4)
    e_half_power = Entry(frame_3_2, width=4)

    e_one_fifth_appearance = Entry(frame_3_2, width=4)
    e_one_fifth_education = Entry(frame_3_2, width=4)
    e_one_fifth_intelligence = Entry(frame_3_2, width=4)
    e_one_fifth_power = Entry(frame_3_2, width=4)

    l_appearance.grid(row=0, column=0, stick=E, padx=4)
    l_education.grid(row=1, column=0, stick=E, padx=4)
    l_intelligence.grid(row=2, column=0, stick=E, padx=4)
    l_power.grid(row=3, column=0, stick=E, padx=4)

    e_appearance.grid(row=0, column=1)
    e_education.grid(row=1, column=1)
    e_intelligence.grid(row=2, column=1)
    e_power.grid(row=3, column=1)

    e_half_appearance.grid(row=0, column=2)
    e_half_education.grid(row=1, column=2)
    e_half_intelligence.grid(row=2, column=2)
    e_half_power.grid(row=3, column=2)

    e_one_fifth_appearance.grid(row=0, column=3)
    e_one_fifth_education.grid(row=1, column=3)
    e_one_fifth_intelligence.grid(row=2, column=3)
    e_one_fifth_power.grid(row=3, column=3)

    #frame_3_3
    l_luck = Label(frame_3_3, text="Szczęście:")
    e_luck = Entry(frame_3_3, width=5)
    e_half_luck = Entry(frame_3_3, width=4)
    e_one_fifth_luck = Entry(frame_3_3, width=4)

    e_luck.bind('<Return>', lambda event:callback(event, e_luck, e_half_luck, e_one_fifth_luck))

    l_luck.grid(row=1, column=0)
    e_luck.grid(row=1, column=1, stick=W)
    e_half_luck.grid(row=1, column=2, stick=W)
    e_one_fifth_luck.grid(row=1, column=3, stick=W)

    #frame_3_4
    btn_fourth_window = Button(frame_3_4, text="Dalej", width=10, command=lambda: to_window(3))
    btn_back_window_2 = Button(frame_3_4, text="Cofnij", width=10, command=lambda: to_window(2))
    btn_random_values_window_3 = Button(frame_3_4, text="Random", width=20, command=lambda: random(3))

    btn_fourth_window.grid(row=0, column=1, pady=20, padx=50, stick=E)
    btn_back_window_2.grid(row=0, column=0, pady=20, padx=50, stick=W)
    btn_random_values_window_3.grid(row=1, column=0, columnspan=2, pady=5)



def fourth_window():

    global frame_4

frame = Label(root)
frame.place(relx=0.5, rely=0.4, anchor=CENTER)

btn_second_window = Button(frame, text="Stwórz postać krok po kroku", command=lambda: to_window(1))
btn_random_charackter = Button(frame, text="Wygeneruj losową postać", command=to_window)
btn_close = Button(frame, text="Zamknij", command=close_program)

btn_second_window.grid(row=0, column=0, pady=2, sticky=W+E+N+S)
btn_random_charackter.grid(row=1, column=0, pady=2, stick=W+E+N+S)
btn_close.grid(row=2, column=0, pady=2, stick=W+E+N+S)



root.mainloop()