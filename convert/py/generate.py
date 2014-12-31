__author__ = 'Henrik'


def file_name(json_name):
    return json_name.lower() + ".py"


def header(namespace, filename):
    return ("import json\n\n"
            "class {0}:\n"
            "    def __init__(self):\n"
            "").format(filename)


def footer():
    return ""


def list(name, type, output):
    output[0] += "        self._{0} = []\n".format(name)
    output[1] += _getter_setter(name)


def string(name, output):
    output[0] += "        self._{0} = \"\"\n".format(name)
    output[1] += _getter_setter(name)


def int(name, output):
    output[0] += "        self._{0} = 0\n".format(name)
    output[1] += _getter_setter(name)


def bool(name, output):
    output[0] += "        self._{0} = False\n".format(name)
    output[1] += _getter_setter(name)

def _getter_setter(name):
    return "    @property\n    def {0}(self):\n        return self._{0}\n    @{0}.setter\n    def {0}(self, value):\n        self._{0} = value\n\n".format(name)