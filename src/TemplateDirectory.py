
from .TemplateFile import * 

import os 

class TemplateDirectory:
    def __init__(self, path):
        self.path = path
    
    def get_relative_root(self, root):
        result = ""
        while not os.path.samefile(root, os.path.split(self.path)[0]):
            result = os.path.join(os.path.split(root)[1], result) 
            root = os.path.split(root)[0]
        return result

    def generate(self, destination_dir_path, params):
        for root, dirs, files in os.walk(self.path):
            my_root = self.get_relative_root(root)
            print(root + " -> " + my_root)
            for k,v in params.items():
                try:
                    my_root = my_root.replace("___%s___" % k , v)
                except TypeError:
                    pass
            # first make path 
            os.makedirs(os.path.join(destination_dir_path, my_root), exist_ok=True)
            for name in files:
                template = TemplateFile(os.path.join(root, name))
                template.generate(os.path.join(destination_dir_path, my_root), params)