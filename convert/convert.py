import os
import glob
import json
import importlib
from collections import OrderedDict
from base.parsedobject import ParsedObject, ParsedObjectType
from base.enginegenerator import BaseEngineGenerator


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
    try:
        json_objects = _load_json_files(json_path)
        for j in json_objects:
            parsed = parse(j)
            result = generate(namespace, targets, parsed)
            _save_to_disk(result, targets)
    finally:
        print "Done"


def generate(namespace, targets, parsed_object):
    """
    Generates a list of content which should be saved to disk
    :param namespace:
    :param targets:
    :param parsed_object:
    :return:
    """
    languages = targets.keys()
    generators = []
    engines = []
    for lang in languages:
        generator_path = "convert.{0}.generator".format(lang)
        factories = []
        for engine in targets[lang]['engines']:
            factory_path = "convert.{0}.{1}.factorygenerator".format(lang, engine)

            factories.append(importlib.import_module(factory_path).FactoryGenerator())

        generators.append(importlib.import_module(generator_path).Generator(factories))

    content = _generate_class(namespace, generators, parsed_object)

    return content


def _generate_class(namespace, generators, parsed_object):
    if parsed_object.skip:
        print "ParsedObject {0} is marked with skip so wont generate a file for this one".format(parsed_object.name)
        return []

    print "Generating {0}.{1}".format(namespace, parsed_object.name)

    content = []

    if parsed_object.type == ParsedObjectType.Object or parsed_object.type == ParsedObjectType.Array:
        for obj in parsed_object.data:
            if obj.type == ParsedObjectType.Object:
                content.extend(_generate_class(namespace, generators, obj))
            elif obj.type == ParsedObjectType.Array:
                for child in obj.data:
                    content.extend(_generate_class(namespace, generators, child))

        print "Generating {0}.{1}".format(namespace, parsed_object.name)
        for generator in generators:
            content.append({"name": generator.file_name(parsed_object.name),
                            "content": generator.generate_code(namespace, parsed_object),
                            "module": generator.__module__})

    return content


def parse(json_object):
    """
    Returns a list representing the generated content for the file which is to be saved to disk.
    :param json_object:
    :rtype: ParsedObject
    :return:
    """
    stripped_filename = os.path.splitext(os.path.basename(json_object["name"]))[0]

    return ParsedObject(stripped_filename, json_object["content"])


def _save_to_disk(result, targets):
    for f in result:
        out_path = ""
        for target in targets:
            if target in f['module']:
                out_path = targets[target]['path']
        out = open(out_path + "/" + f["name"], "w+")
        out.write(f["content"])
        out.close()


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
        file_content = {"name": json_path, "content": json.loads(f.read(), object_pairs_hook=OrderedDict)}
        json_objects.append(file_content)
        f.close()
    return json_objects