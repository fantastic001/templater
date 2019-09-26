from ..tps.parser import String, Integer, Boolean, Object, List, parse_tps_file


class GUIStateMachine:
    def __init__(self):
        self.listeners = []
        self.result = {}

    def add_listener(self, listener):
        self.listeners.append(listener)

    def execute_file(self, filename):
        self.execute(parse_tps_file(filename))

    def set_result(self, dict_result):
        self.result = dict_result

    def execute(self, tps_object):
        for listener in self.listeners:
            listener.initialize_dialog(tps_object)
            for param in tps_object.params:
                ptype = param.ptype
                name = param.name
                label = param.name.replace("_", " ")
                if isinstance(ptype, Integer):
                    listener.handle_integer(name, label, param.default)
                elif isinstance(ptype, String):
                    listener.handle_string(name, label, param.default)
                elif isinstance(ptype, Boolean):
                    listener.handle_boolean(name, label, param.default)
                elif isinstance(ptype, Object):
                    listener.handle_object(name, label, param.default)
                elif isinstance(ptype, List):
                    listener.handle_list(name, llabel, param.default)
                else:
                    raise ValueError("Wrong parameter type for parameter %s" % param.name)
            listener.finalize_gui(self)
            
            # this will block until gui is finished, listeners should call set_result(dict_object) of provided sm parameter provided in finalize_gui 
            listener.show_gui()
            print(self.result)
