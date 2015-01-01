from convert.base.generator import BaseGenerator


class Generator(BaseGenerator):
    pass


def file_name(json_name):
    return json_name.lower() + ".py"


def header(namespace, filename):
    return ("import json\n\n"
            "class {0}:\n"
            "    def __init__(self, json_obj):\n"
            "").format(filename)


def footer():
    return "    def toString(self):\n        #todo implement!\n"


def begin_class(name, output):
    output[0] += "class {0}:\n".format(name)

def end_class(name, output):
    pass


def list(name, type, output):
    output[0] += "        self._{0} = json_obj[\"{0}\"]\n".format(name)
    output[1] += _getter_setter(name)


def string(name, output):
    output[0] += "        self._{0} = json_obj[\"{0}\"]\n".format(name)
    output[1] += _getter_setter(name)


def int(name, output):
    output[0] += "        self._{0} = json_obj[\"{0}\"]\n".format(name)
    output[1] += _getter_setter(name)


def bool(name, output):
    output[0] += "        self._{0} = json_obj[\"{0}\"]\n".format(name)
    output[1] += _getter_setter(name)

def _getter_setter(name):
    return "    @property\n    def {0}(self):\n        return self._{0}\n    @{0}.setter\n    def {0}(self, value):\n        self._{0} = value\n\n".format(name)

#a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
#a.sub(r'_\1', 'HTTPResponseCodeXYZ').lower()