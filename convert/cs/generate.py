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
            "        public {1}(JSONNode jsonObject)\n"
            "        {{\n"
            "").format(namespace, filename)


def footer():
    return ("    }\n"
            "}\n")


def begin_class(name, output):
    output[0] += "public class {0}\n{{\n".format(name)

def end_class(name, output):
    output[0] += "}\n"


def list(name, type, output):
    output[0] += "            {0} = jsonObject[\"{0}\"];\n".format(name)
    output[1] += "public List<{0}> {1} {{get; set;}}\n".format(type, name)


def string(name, output):
    output[0] += "            {0} = jsonObject[\"{0}\"];\n".format(name)
    output[1] += "public string {0} {{get; set;}}\n".format(name)


def int(name, output):
    output[0] += "            {0} = jsonObject[\"{0}\"];\n".format(name)
    output[1] += "public int {0} {{get; set;}}\n".format(name)


def bool(name, output):
    output[0] += "            {0} = jsonObject[\"{0}\"];\n".format(name)
    output[1] += "public bool {0} {{get; set;}}\n".format(name)