#!/usr/bin/env python 

import sys 
import os 
import jinja2
import os.path
import json 
from ArgumentStack import * 

from src import * 
from src.sources import * 

stack = ArgumentStack("Wrong command") 
stack.popAll()
stack.pushCommand("help")
stack.assignAction(lambda: print(stack.getHelp()), "Get help")
stack.popAll()


def do_template(template, output, params):
    t = DirectoryTemplateSource("./templates").get_template(template)
    if t is not None:
        t.generate(output, params)
    else:
        print("Error: template not found")

stack.pushCommand("create")
stack.pushVariable("template")
stack.pushVariable("output")
stack.pushCommand("json")
stack.pushVariable("json_file_path")
def create_from_template_using_json(template, output, json_file_path):
    params = {}
    with open(json_file_path) as f:
        params = json.loads(f.read())
    do_template(template, output, params)
stack.assignAction(create_from_template_using_json, "Generate from template where parameters are in specified json file")    

stack.pop()
stack.pop()
stack.pushVariable("params_string")
def create_from_template_using_string(template, output, params_string):
    params = {s.split("=")[0].strip(): s.split("=")[1].strip() for s in params_string.split(" ")}
    do_template(template, output, params)
stack.assignAction(create_from_template_using_string, "Generate from template with parameters specified as string like 'p1=v1 p2=v2'")
stack.execute(sys.argv)
