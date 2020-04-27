from tkinter import *

from base_window import BaseWindow


class SkillsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.create_content()

    def create_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)