from model import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def ask_if_ready():

    response = messagebox.askyesno("Ready to Run", "Are you ready to run the program?")


    if response:
        app_settings["run"] = True
        running()
    root = tk.Tk()
    root.withdraw()
    ask_if_ready()
    root.mainloop()

#def main_window():
#    mainroot = tk.Tk()






