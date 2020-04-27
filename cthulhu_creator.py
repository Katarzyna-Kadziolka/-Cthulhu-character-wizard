from tkinter import *
import sqlite3
from random_calculator import RandomCalculator
from database import Database
from home_window import HomeWindow


root = Tk()
root.title("Kreator Badaczy Tajemnic")
root.geometry("400x500")


calculator = RandomCalculator()
database = Database()
home_window = HomeWindow(root)


root.mainloop()