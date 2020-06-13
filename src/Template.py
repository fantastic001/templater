

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
        files = os.listdir(self.path)
        if "META_PRE.sh" in files:
            import subprocess
            print("Executing script %s" % os.path.join(self.path, "META_PRE.sh"))
            ret = subprocess.Popen(["/".join([self.path, "META_PRE.sh"])], cwd=destination_dir_path).wait()
            if ret != 0:
                print("Preprocessing hook failed: error %d" % ret)
                return
        for name in os.listdir(self.path):
            fullpath = os.path.join(self.path, name)
            if name in ["META_PRE.sh", "META_POST.sh", self.params_file]:
                continue
            if os.path.isdir(fullpath):
                template = TemplateDirectory(fullpath)
                template.generate(destination_dir_path, params)
            else:
                template = TemplateFile(fullpath)
                template.generate(destination_dir_path, params)
        if "META_POST.sh" in files:
            import subprocess
            print("Executing script %s" % os.path.join(self.path, "META_POST.sh"))
            ret = subprocess.Popen(["/".join([self.path, "META_POST.sh"])], cwd=destination_dir_path).wait()
            if ret != 0:
                print("Postprocessing hook failed: error %d" % ret)
                return
    def get_params_path(self):
        import tempfile, shutil, os
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "TPS_TEMP_FILE_%d.tps" % self.H)
        return temp_path
    
    def __del__(self):
        os.remove(self.get_params_path())

