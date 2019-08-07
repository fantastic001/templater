#!/usr/bin/env python 

import sys 
import os 
import jinja2
import os.path
import json 

from src import * 

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

template = None
if os.path.isdir(path):
    template = TemplateDirectory(path)
else:
    template = TemplateDirectory(path)

template.generate(output, params)