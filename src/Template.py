

import os 
import os.path
from .TemplateFile import * 
from .TemplateDirectory import * 
import datetime


class Template:

    def __init__(self, path, params_file = "params.tps"):
        self.path = path
        self.params_file = params_file
        self.H = abs(hash(datetime.datetime.now()))
        path = os.path.join(self.path, self.params_file)
        with open(path) as f:
            with open(self.get_params_path(), "w") as tmp:
                tmp.write(f.read())
    def generate(self, destination_dir_path, params):
        for name in os.listdir(self.path):
            fullpath = os.path.join(self.path, name)
            if name == self.params_file:
                continue
            if os.path.isdir(fullpath):
                template = TemplateDirectory(fullpath)
                template.generate(destination_dir_path, params)
            else:
                template = TemplateFile(fullpath)
                template.generate(destination_dir_path, params)
    def get_params_path(self):
        import tempfile, shutil, os
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "TPS_TEMP_FILE_%d.tps" % self.H)
        return temp_path
    
    def __del__(self):
        os.remove(self.get_params_path())

