__author__ = 'Henrik'


def file_name(json_name):
    return json_name + ".cs"


def header(namespace, filename):
    return ("using System.Collections.Generic;\n"
            "using SimpleJSON;\n\n"
            "public namespace {0}\n"
            "{{\n"
            "    public class {1}\n"
            "    {{\n"
            "").format(namespace, filename)


def footer():
    return ("    }\n"
            "}\n")


def list(name, type, output):
    return "public List<{0}> {1} {{get; set;}}\n".format(type, name)


def string(name, output):
    return "public string {0} {{get; set;}}\n".format(name)


def int(name, output):
    return "public int {0} {{get; set;}}\n".format(name)


def bool(name, output):
    return "public bool {0} {{get; set;}}\n".format(name)