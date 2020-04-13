from tkinter import Frame, END


class BaseWindow:

    def __init__(self, root):
        self.root = root
        self.frame = Frame(root)

    def move_to_window(self, window):
        self.frame.destroy()
        window.create_content()

    def create_content(self):
        pass

    def set_text(self, entry, text):
        entry.delete(0, END)
        entry.insert(0, text)

