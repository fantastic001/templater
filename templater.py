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

stack.pop()
stack.pop()
def create_from_template_using_dialog(template, **kw):
    params = {} # TODO get parameters from GUI created from template
    do_template(template, os.getcwd(), params)
stack.assignAction(create_from_template_using_dialog, "Generate from template in current directory using GUI dialog")
stack.popAll()

stack.pushCommand("verify")
stack.pushCommand("tps")
stack.pushVariable("path")
def verify_tps(path, **kw):
    # TODO implement
    pass
stack.assignAction(verify_tps, "Verify TPS file")
stack.pop()
stack.pop()

stack.pushCommand("json")
stack.pushVariable("tps_path")
stack.pushVariable("json_path")
def verify_json(tps_path, json_path, **kw):
    # TODO implement
    pass
stack.assignAction(verify_json, "Verify if JSON file coontains all parameters specified in TPS")
stack.popAll()
stack.execute(sys.argv)
