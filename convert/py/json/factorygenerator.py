import re
from convert.base.factorygenerator import BaseFactoryGenerator
from convert.base.parsedobject import ParsedObjectType


class FactoryGenerator(BaseFactoryGenerator):
    def generate_import(self):
        return "import json\n"

    def _generate_from_json(self):
        constructor = ("        @staticmethod\n"
                       "        def from_json(json_obj):\n"
                       "            \"\"\":type json_obj: dict\n"
                       "               :rtype: {0}\"\"\"\n"
                       "            if json_obj is None:\n"
                       "                return None\n"
                       "            obj = {0}()\n").format(_capitalize(self.data.name))

        for member in self.data.data:
            constructor += _member_load(member)

        constructor += "            return obj\n\n"

        return constructor

    def _generate_to_json(self):
        result = ("        @staticmethod\n"
                  "        def to_json(self):\n"
                  "            \"\"\":rtype: dict\"\"\"\n"
                  "            return {0}.JsonFactory.JsonEncoder().encode(self)\n\n"
                  "        class JsonEncoder(json.JSONEncoder):\n"
                  "            def default(self, obj):\n"
                  "                if obj is None:\n"
                  "                    return None\n"
                  "                d = {{\n").format(_capitalize(self.data.name))
        for member in self.data.data:
            result += _member_save(member)
        result += "                }\n"
        for member in self.data.data:
            if member.type == ParsedObjectType.Array:
                result += _member_save_list(member)
        result += "                return d\n\n"
        return result

    def generate(self, data, namespace):
        self.data = data
        self.namespace = namespace

        serializers = "\n    class JsonFactory():\n"
        serializers += self._generate_to_json()
        serializers += self._generate_from_json()
        return serializers


def _member_load(member):
    json_container_string = "json_obj[\"{0}\"]".format(member.name)
    if member.type == ParsedObjectType.Object:
        return ("            if \"{3}\" in json_obj:\n"
                "                obj._{0} = {1}.JsonFactory.from_json({2})\n").format(_camel_case(member.name), _capitalize(member.name), json_container_string, member.name)
    elif member.type == ParsedObjectType.Array:
        result = ("            if \"{2}\" in json_obj:\n"
                  "                obj._{0} = []\n"
                  "                for item in {1}:\n").format(_camel_case(member.name), json_container_string, member.name)
        child = member.data[0]

        if child.type == ParsedObjectType.Object:
            result += "                    obj._{0}.append({1}.JsonFactory.from_json(item))\n".format(_camel_case(member.name), _capitalize(child.name))
        else:
            result += "                    obj._{0}.append(item)\n".format(_camel_case(member.name))
        return result
    else:
        return ("            if \"{2}\" in json_obj:\n"
                "                obj._{0} = {1}\n").format(_camel_case(member.name), json_container_string, member.name)


def _member_save(member):
    if member.type == ParsedObjectType.Object:
        return "                    '{0}': {2}.JsonFactory.JsonEncoder().default(obj.{1}),\n".format(member.name, _camel_case(member.name), _capitalize(member.name))
    if member.type == ParsedObjectType.Array:
        return "                    '{0}': [],\n".format(member.name)
    return "                    '{0}': obj.{1},\n".format(member.name, _camel_case(member.name))


def _camel_case(obj):
    a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
    return a.sub(r'_\1', obj).lower()


def _member_save_list(member):
    result = "                for item in obj.{1}:\n".format(member.name, _camel_case(member.name))

    child = member.data[0]
    if child.type == ParsedObjectType.Object:
        result += "                    d['{0}'].append({1}.JsonFactory.JsonEncoder().default(item))\n".format(member.name, _capitalize(child.name))
    else:
        result += "                    d['{0}'].append(item)\n".format(member.name)
    result += "\n"
    return result


def _capitalize(obj):
    """
    Returns the object name with the first letter capitalized (all other untouched).
    :param obj:
    :return:
    """
    if obj.__len__() < 2:
        return obj
    if obj == "string" or obj == "float" or obj == "int":
        return obj
    return obj[0].upper() + obj[1:]

