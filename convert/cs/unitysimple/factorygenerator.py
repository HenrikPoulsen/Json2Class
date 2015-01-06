from convert.base.factorygenerator import BaseFactoryGenerator
from convert.base.parsedobject import *


class FactoryGenerator(BaseFactoryGenerator):
    def generate(self, data, namespace):
        """

        :type data: ParsedObject
        :return:
        """
        self.data = data
        self.namespace = namespace
        serializers = ("\n        public static class SimpleJsonFactory\n"
                       "        {\n")
        serializers += self._generate_to_json()
        serializers += self._generate_from_json()
        serializers += "        }\n"
        return serializers

    def _generate_to_json(self):
        serializer = ("            public static JSONNode ToJson({0} obj)\n"
                      "            {{\n"
                      "                var json = new JSONClass();\n").format(_capitalize(self.data.name))
        for member in self.data.data:
            if member.type == ParsedObjectType.Object:
                serializer += _serialize_object_member(member, self.namespace)
            elif member.type == ParsedObjectType.Array:
                serializer += _serialize_array_member(member, self.namespace)
            else:
                serializer += "                json[\"{0}\"] = new JSONData(obj.{1});\n".format(member.name, _capitalize(member.name))

        serializer += ("                return json;\n"
                       "            }\n\n")
        return serializer

    def _generate_from_json(self):
        serializer = ("            public static {0} FromJson(JSONNode json)\n"
                      "            {{\n").format(_capitalize(self.data.name))

        # member initialization
        for member in self.data.data:
            serializer += _member_initialization(member, self.namespace)

        serializer += ("                return new {0}\n"
                       "                {{\n").format(_capitalize(self.data.name))

        for member in self.data.data:
            serializer += "                    {0} = {1},\n".format(_capitalize(member.name), member.name)
        serializer += ("                };\n"
                       "            }\n\n")

        return serializer


def _member_declaration(member):
    return "        public {0} {1} {{get; set;}}\n".format(_get_type_name(member), _capitalize(member.name))


def _member_initialization(member, namespace):
    """
    Generated the code for initialization of the members in the constructor.
    :type member: ParsedMember
    :param member:
    :return:
    """
    json_container_string = "json[\"{0}\"]".format(member.name)

    if member.type == ParsedObjectType.Object:
        return "                var {0} = {3} != null ? {1}.{2}.SimpleJsonFactory.FromJson({3}) : null;\n".format(member.name, namespace, _capitalize(member.name), json_container_string)
    elif member.type == ParsedObjectType.Array:
        result = ("                var {2} = {1}();\n"
                  "                foreach(JSONNode item in json[\"{2}\"].AsArray)\n"
                  "                {{\n").format(_capitalize(member.name), _get_member_initialization_string(member, json_container_string), member.name)
        child = member.data[0]

        if child.type == ParsedObjectType.Object:
            result += "                    {0}.Add({1}.{2}.SimpleJsonFactory.FromJson(item));\n".format(member.name, namespace, _capitalize(child.name))
        else:
            result += "                    {0}.Add(item{1});\n".format(member.name, _json_load_as(child))
        result += "                }\n\n"
        return result
    elif member.type == ParsedObjectType.String:
        return "                var {0} = {1}.Value ?? \"\";\n".format(member.name, _get_member_initialization_string(member, json_container_string))
    else:
        return "                var {0} = {1};\n".format(member.name, _get_member_initialization_string(member, json_container_string))
        return result


def _get_member_initialization_string(member, json_container):
    if member.type == ParsedObjectType.Object:
        return "new {0}({1})".format(_capitalize(member.name), json_container)
    if member.type == ParsedObjectType.Array:
        return "new {0}".format( _get_type_name(member))
    return "{0}{1}".format(json_container, _json_load_as(member))


def _json_load_as(member):
    """
    Returns the property to be called when loading this object from a JSONNode.
    For example: MyFloat = jsonObject["myFloat"].AsFloat;
    :param member:
    :return:
    """
    if member.type == ParsedObjectType.Float:
        return ".AsFloat"
    elif member.type == ParsedObjectType.Int:
        return ".AsInt"
    elif member.type == ParsedObjectType.Bool:
        return ".AsBool"
    return ""



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


def _serialize_object_member(member, namespace):
    return "                json[\"{0}\"] = obj.{1} != null ? {2}.{1}.SimpleJsonFactory.ToJson(obj.{1}) : null;\n".format(member.name, _capitalize(member.name), namespace)


def _serialize_array_member(member, namespace):
    serializer = "                var {0} = new JSONArray();\n".format(member.name)
    serializer += "                foreach(var item in obj.{0})\n".format(_capitalize(member.name))
    serializer += "                {\n"
    if member.data[0].type == ParsedObjectType.Object:
        serializer += "                    {0}.Add({1}.{2}.SimpleJsonFactory.ToJson(item));\n".format(member.name, namespace, _capitalize(member.data[0].name))
    else:
        serializer += "                    {0}.Add(new JSONData(item));\n".format(member.name)
    serializer += "                }\n"
    serializer += "                json[\"{0}\"] = {0};\n\n".format(member.name)
    return serializer

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


def _json_save_as(member):
    """
    Returns the property to be called when loading this object from a JSONNode.
    For example: MyFloat = jsonObject["myFloat"].AsFloat;
    :param member:
    :return:
    """
    if member.type == ParsedObjectType.Float:
        return ".AsFloat"
    elif member.type == ParsedObjectType.Int:
        return ".AsInt"
    elif member.type == ParsedObjectType.Bool:
        return ".AsBool"
    elif member.type == ParsedObjectType.Object:
        return ".ToJson()"
    return ""