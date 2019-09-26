
import tkinter as tk 
from .GUIListener import *

class TkListener(GUIListener):
    def initialize_dialog(self, tps_object):
        self.root = tk.Tk()
        

    def handle_integer(self, name, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    def handle_string(self, name, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    def handle_boolean(self, name, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = tk.Checkbutton(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    def handle_object(self, name, value):
        print("Object")
    def handle_list(self, name, value):
        print("List")

    def show_gui(self):
        self.root.mainloop()
