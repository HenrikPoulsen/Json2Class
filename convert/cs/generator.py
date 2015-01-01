from convert.base.generator import BaseGenerator
from convert.base.parsedclass import ParsedClass
from convert.base.parsedmember import ParsedMember


class Generator(BaseGenerator):
    def __init__(self):
        self.data = None
        self.namespace = ""

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

                "").format(self.namespace, _capitalize(self.data))

    def _generate_constructor(self):
        constructor = ("        public {0}(JSONNode jsonObject)\n"
                        "        {{\n").format(_capitalize(self.data))

        # member initialization
        for member in self.data.members:
            constructor += _member_initialization(member)

        constructor += "        }\n\n"
        return constructor

    def _generate_properties(self):
        properties = ""
        for member in self.data.members:
            properties += _member_declaration(member)
        return properties

    def _generate_serializers(self):
        serializer = ("\n        public JSONNode ToJson()\n"
                      "        {\n"
                      "            var json = JSON.Parse(\"{}\");\n")

        for member in self.data.members:
            if isinstance(member, ParsedClass):
                serializer += "            json[\"{0}\"] = {1}.ToJson();\n".format(member.name, _capitalize(member))
            else:
                serializer += "            json[\"{0}\"]{2} = {1};\n".format(member.name, _capitalize(member), _json_save_as(member))

        serializer += ("            return json;\n"
                       "        }\n")

        return serializer


    def _generate_footer(self):
        return ("    }\n"
                "}\n")

def _member_declaration(member):
    return "        public {0} {1} {{get; set;}}\n".format(_get_type_name(member), _capitalize(member))

def _member_initialization(member):
    """
    Generated the code for initialization of the members in the constructor.
    :type member: ParsedMember
    :param member:
    :return:
    """
    if isinstance(member, ParsedClass):
        return "            {0} = new {0}(jsonObject[\"{1}\"]);\n".format(_capitalize(member), member.name)
    else:
        return "            {0} = jsonObject[\"{1}\"]{2};\n".format(_capitalize(member), member.name, _json_load_as(member))

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
    return obj.name[0].upper() + obj.name[1:]


def _get_type_name(obj):
    """
    If a ParsedClass is supplied then it returns the object name with a captialized first letter (myClass => MyClass)
    For ParsedMember it returns the type of the member (myString => string)
    :param obj:
    :return:
    """
    if isinstance(obj, ParsedClass):
        return _capitalize(obj)
    elif isinstance(obj, ParsedMember):
        return obj.type