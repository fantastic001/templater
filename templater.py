#!/usr/bin/env python 

import sys 
import os 
import jinja2
import os.path
import json 

if len(sys.argv) < 3 or sys.argv[1] == "--help":
    print("Usage: templater input_template output param1=value1 param2=value2 ...")
    exit(0)

path = os.path.abspath(sys.argv[1])
output = sys.argv[2]
params = {}
if os.path.isfile(sys.argv[3]):
    with open(sys.argv[3]) as f:
        params = json.loads(f.read())
        x = {s.split("=")[0].strip(): s.split("=")[1].strip() for s in sys.argv[4:]}
        params = dict(**params, **x)
else:
    params = {s.split("=")[0].strip(): s.split("=")[1].strip() for s in sys.argv[3:]}

def generate(path, output, params):
    for k,v in params.items():
        output = output.replace("___%s___" % k, v)
    input_file = open(path)
    contents = input_file.read()
    output_file = open(output, "w")
    output_file.write(jinja2.Template(contents).render(**params))

if os.path.isdir(path):
    for root, dirs, files in os.walk(path):
        print(root)
        my_root = os.path.abspath(root).replace(path, output)
        for k,v in params.items():
            my_root = my_root.replace("___%s___" % k , v)
        # first make path 
        os.makedirs(my_root, exist_ok=True)
        for name in files:
            print("Generating file %s" % os.path.join(my_root, name))
            generate(os.path.join(root, name), os.path.join(my_root, name), params)
else:
    generate(path, output, params)