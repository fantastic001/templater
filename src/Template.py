

import os 
import os.path
from .TemplateFile import * 
from .TemplateDirectory import * 
class Template:

    def __init__(self, path):
        self.path = path

    def generate(self, destination_dir_path, params):
        for name in os.listdir(self.path):
            fullpath = os.path.join(self.path, name)
            if os.path.isdir(fullpath):
                template = TemplateDirectory(fullpath)
                template.generate(destination_dir_path, params)
            else:
                template = TemplateFile(fullpath)
                template.generate(destination_dir_path, params)