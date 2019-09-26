
from src.gui.GUIStateMachine import *
from src.gui.TkListener import * 

sm = GUIStateMachine()

sm.add_listener(TkListener())

sm.execute_file("example.tps")
