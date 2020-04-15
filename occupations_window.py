from tkinter import *
from base_window import BaseWindow


class OccupationsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.create_content()
