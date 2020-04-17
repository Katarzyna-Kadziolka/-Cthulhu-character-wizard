from tkinter import *
from base_window import BaseWindow


class OccupationsWindow(BaseWindow):

    def __init__(self, root):
        super().__init__(root)
        self.create_content()

    def create_content(self):
        self.frame = Label(self.root)
        self.frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        frame_1 = Label(self.frame)
        frame_1.grid(row=0, column=0, columnspan=2)
        frame_2 = Label(self.frame)
        frame_2.grid(row=1, column=0, rowspan=2)
        frame_3 = Label(self.frame)
        frame_3.grid(row=1, column=1)
        frame_4 = Label(self.frame)
        frame_4.grid(row=2, column=1)

        #frame_1
        label_title = Label(frame_1, text="Wybór zawodu", font=("Helvetica", 11)).grid(row=0, column=0, pady=10)

        #frame_2
        scrollbar = Scrollbar