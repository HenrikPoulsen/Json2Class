from convert.base.generator import BaseGenerator
from convert.base.parsedobject import *
from convert.base.parsedmember import ParsedMember


class Generator(BaseGenerator):
    def __init__(self):
        self.data = None
        self.namespace = ""

    def file_name(self, name):
        return name[0].upper() + name[1:] + ".cs"

    def generateCode(self, namespace, data):
        """

        :type data: ParsedClass
        :return:
        """
        self.data = data
        self.namespace = namespace
        return "".join([self._generate_header(), self._generate_constructor(), self._generate_properties(), self._generate_serializers(), self._generate_footer()])
        print "Creating class {0}".format(data.name)

    def _file_name(self):
        return self.data.name + ".cs"

    def _generate_header(self):
        return ("using System.Collections.Generic;\n"
                "using SimpleJSON;\n\n"
                "namespace {0}\n"
                "{{\n"
                "    public class {1}\n"
                "    {{\n"

                "").format(self.namespace, _capitalize(self.data.name))

    def _generate_constructor(self):
        constructor = ("        public {0}(JSONNode jsonObject)\n"
                        "        {{\n").format(_capitalize(self.data.name))

        # member initialization
        for member in self.data.data:
            constructor += _member_initialization(member)

        constructor += "        }\n\n"
        return constructor

    def _generate_properties(self):
        properties = ""
        for member in self.data.data:
            properties += _member_declaration(member)
        return properties

    def _generate_serializers(self):
        serializer = ("\n        public JSONNode ToJson()\n"
                      "        {\n"
                      "            var json = JSON.Parse(\"{}\");\n")

        for member in self.data.data:
            if member.type == ParsedObjectType.Object:
                serializer += "            json[\"{0}\"] = {1}.ToJson();\n".format(member.name, _capitalize(member.name))
            else:
                serializer += "            json[\"{0}\"]{2} = {1};\n".format(member.name, _capitalize(member.name), _json_save_as(member))

        serializer += ("            return json;\n"
                       "        }\n")

        return serializer


    def _generate_footer(self):
        return ("    }\n"
                "}\n")

def _member_declaration(member):
    return "        public {0} {1} {{get; set;}}\n".format(_get_type_name(member), _capitalize(member.name))

def _member_initialization(member):
    """
    Generated the code for initialization of the members in the constructor.
    :type member: ParsedMember
    :param member:
    :return:
    """
    if member.type == ParsedObjectType.Object:
        return "            {0} = new {0}(jsonObject[\"{1}\"]);\n".format(_capitalize(member.name), member.name)
    else:
        return "            {0} = jsonObject[\"{1}\"]{2};\n".format(_capitalize(member.name), member.name, _json_load_as(member))

def _json_load_as(member):
    """
    Returns the property to be called when loading this object from a JSONNode.
    For example: MyFloat = jsonObject["myFloat"].AsFloat;
    :param member:
    :return:
    """
    if member.type == "float":
        return ".AsFloat"
    elif member.type == "int":
        return ".AsInt"
    elif member.type == "bool":
        return ".AsBool"
    return ""

def _json_save_as(member):
    """
    Returns the property to be called when loading this object from a JSONNode.
    For example: MyFloat = jsonObject["myFloat"].AsFloat;
    :param member:
    :return:
    """
    if member.type == "float":
        return ".AsFloat"
    elif member.type == "int":
        return ".AsInt"
    elif member.type == "bool":
        return ".AsBool"
    return ""


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


def _get_type_name(member):
    """
    If a ParsedClass is supplied then it returns the object name with a captialized first letter (myClass => MyClass)
    For ParsedMember it returns the type of the member (myString => string)
    :type member: ParsedMember
    :param obj:
    :return:
    """
    if member.type == ParsedObjectType.String or member.type == ParsedObjectType.Int or member.type == ParsedObjectType.Float:
        return member.type.name.lower()
    elif member.type == ParsedObjectType.Array:
        return "List<{0}>".format(_get_type_name(member.data[0]))
    else:
        return _capitalize(member.name)