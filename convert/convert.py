import os,sys,imp
import glob
import json
import importlib


def run(namespace, targets, json_path):
    """
    :type namespace: str
    :param namespace:
    :type targets: dict
    :param targets:
    :type json_path: str
    :param json_path:
    :return:
    """
    json_objects = []
    languages = targets.keys()
    try:
        json_objects = _load_json_files(json_path)
        for j in json_objects:
            generate(namespace, languages, j)
    finally:
        print "Done"

    #for lang in targets.keys():
    #    files = load_files(targets[lang])

def generate(namespace, languages, json_object):
    """
    Returns a list representing the generated content for the file which is to be saved to disk.
    :param namespace:
    :param languages:
    :param json_object:
    :rtype: list
    :return:
    """
    output = {}
    # First we get the proper filename for the class and generate the header and footer of the class
    for lang in languages:
        mod = importlib.import_module("convert."+lang+".generate")
        stripped_filename = os.path.splitext(os.path.basename(json_object["name"]))[0]
        file_name = mod.file_name(stripped_filename)
        output[file_name] = {"mod": mod}
        output[file_name]["generated"] = [mod.header(namespace, stripped_filename)]
        output[file_name]["generated"].append("")
        output[file_name]["generated"].append(mod.footer())

    # Now we start iterating the json object to generate our class content
    _parse_type(json_object["content"], output)

    return output


def _parse_dict(obj, output, name=None):
    #print "public class " + str(name) + "{"
    for key in obj.keys():
        _parse_type(obj[key], output, key)
    #print "}"


def _parse_list(obj, output, name=None):
    for f in output.keys():
        output[f]["mod"].list(name, _type_to_string(type(obj[0])), output[f]["generated"])


def _type_to_string(obj):
    if obj is dict:
        return "class"
    if obj is list:
        return "list"
    if obj is unicode:
        return "string"
    if obj is bool:
        return "bool"
    if obj is int:
        return int
    return "Unknown"

def _parse_int(obj, output, name=None):
    for f in output.keys():
        output[f]["mod"].int(name, output[f]["generated"])


def _parse_string(obj, output, name=None):
    for f in output.keys():
        output[f]["mod"].string(name, output[f]["generated"])

def _parse_type(obj, output, name=None):
    obj_type = type(obj)

    if obj_type is dict:
        _parse_dict(obj, output, name)
    elif obj_type is list:
        _parse_list(obj, output, name)
    elif obj_type is unicode:
        _parse_string(obj, output, name)
    elif obj_type is bool:
        print "Obj " + str(name) + ": " + str(obj_type)
    elif obj_type is int:
        _parse_int(obj, output, name)
    else:
        print "Unknown " + str(obj_type)

def _load_json_files(json_path):
    """
    :type json_path: str
    :param json_path:
    :rtype: list
    :return:
    """
    json_objects = []
    if os.path.isdir(json_path):
        for f in glob.glob(json_path + "/*.json"):
            json_objects.extend(_load_json_files(f))
    else:
        f = open(json_path, mode='r')
        file_content = {"name": json_path, "content": json.load(f)}
        json_objects.append(file_content)
    return json_objects


def _close_files(file_list):
    """
    :type file_list: list
    :param file_list:
    :return:
    """
    for f in file_list:
        f.close()