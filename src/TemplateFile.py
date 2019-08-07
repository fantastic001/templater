
import os 
import os.path
import jinja2 
class TemplateFile:

    def __init__(self, path):
        self.path = path

    def generate(self, destination_dir_path, params):
        output = os.path.split(self.path)[-1]
        for k,v in params.items():
            try:
                output = output.replace("___%s___" % k, v)
            except TypeError:
                pass
        input_file = open(self.path)
        contents = input_file.read()
        print("Extracting %s" % os.path.join(destination_dir_path, output))
        output_file = open(os.path.join(destination_dir_path, output), "w")
        output_file.write(jinja2.Template(contents).render(**params))
