from ..tps.parser import String, Integer, Boolean, Object, List, parse_tps_file


class GUIStateMachine:
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def execute_file(self, filename):
        self.execute(parse_tps_file(filename))

    def execute(self, tps_object):
        for listener in self.listeners:
            listener.initialize_dialog(tps_object)
            for param in tps_object.params:
                ptype = param.ptype
                name = param.name.replace("_", " ")
                if isinstance(ptype, Integer):
                    listener.handle_integer(name, param.default)
                elif isinstance(ptype, String):
                    listener.handle_string(name, param.default)
                elif isinstance(ptype, Boolean):
                    listener.handle_boolean(name, param.default)
                elif isinstance(ptype, Object):
                    listener.handle_object(name, param.default)
                elif isinstance(ptype, List):
                    listener.handle_list(name, param.default)
                else:
                    raise ValueError("Wrong parameter type for parameter %s" % param.name)
            listener.show_gui()
