#!/usr/bin/env python 

import sys 
import os 
import jinja2
import os.path
import json 

from src import * 
from src.sources import * 

if len(sys.argv) < 3 or sys.argv[1] == "--help":
    print("Usage: templater template output param1=value1 param2=value2 ...")
    exit(0)

template = sys.argv[1]
output = sys.argv[2]
params = {}
if os.path.isfile(sys.argv[3]):
    with open(sys.argv[3]) as f:
        params = json.loads(f.read())
        x = {s.split("=")[0].strip(): s.split("=")[1].strip() for s in sys.argv[4:]}
        params = dict(**params, **x)
else:
    params = {s.split("=")[0].strip(): s.split("=")[1].strip() for s in sys.argv[3:]}

t = DirectoryTemplateSource("./templates").get_template(template)
if t is not None:
    t.generate(output, params)
else:
    print("Error: template not found")