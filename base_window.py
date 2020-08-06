from tkinter import Frame, END
from tkinter import *


class BaseWindow:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(root)

    def move_to_window(self, window):
        self.frame.destroy()
        window.create_content()

    def set_text(self, entry, text):
        entry.delete(0, END)
        entry.insert(0, text)

    def check_fill_entry(self, button, entry_list):
        for entry in entry_list:
            if not entry.get():
                button.config(state=DISABLED)
                break
            else:
                button.config(state=NORMAL)
