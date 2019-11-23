

import os 
import os.path
from .TemplateFile import * 
from .TemplateDirectory import * 
class Template:

    def __init__(self, path, params_file = "params.tps"):
        self.path = path
        self.params_file = params_file

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
        return os.path.join(self.path, self.params_file)
