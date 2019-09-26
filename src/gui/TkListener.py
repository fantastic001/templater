
import tkinter as tk 
from .GUIListener import *
from tkinter import ttk

class TkListener(GUIListener):
    def initialize_dialog(self, tps_object):
        self.root = tk.Tk()
        self.result = {} 
        self.generators = []

        

    def handle_integer(self, name, label, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        self.generators.append(( name, lambda: int(ent.get())))
    def handle_string(self, name, label, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        self.generators.append(( name, lambda: str(ent.get())))
    def handle_boolean(self, name, label, value):
        row = tk.Frame(self.root)
        lab = tk.Label(row, width=15, text=name, anchor='w')
        ent = ttk.Checkbutton(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        self.generators.append(( name, lambda: ent.state()[0] == "selected"))
    def handle_object(self, name, label, value):
        print("Object")
    def handle_list(self, name, label, value):
        print("List")

    def finalize_gui(self, sm):
        def clicked():
            for name, f in self.generators:
                self.result[name] = f()
            sm.set_result(self.result)
            self.root.destroy()
        row = tk.Frame(self.root)
        ent = tk.Button(row, text="OK", command=clicked)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)


    def show_gui(self):
        self.root.mainloop()
