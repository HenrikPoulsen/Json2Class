from convert.base.factorygenerator import BaseFactoryGenerator
from convert.base.parsedobject import *


class FactoryGenerator(BaseFactoryGenerator):
    def generate_import(self):
        return "using System.Collections.Generic;\n"

    def generate(self, data, namespace):
        """

        :type data: ParsedObject
        :return:
        """
        self.data = data
        self.namespace = namespace
        serializers = ("\n        public static class FastJSONFactory\n"
                       "        {\n")
        serializers += self._generate_to_json()
        serializers += self._generate_from_json()
        serializers += "        }\n"
        return serializers

    def _generate_to_json(self):
        serializer = ("            public static string ToJson({0} obj)\n"
                      "            {{\n"
                      "                var jsonObject = ToJsonObject(obj);\n"
                      "                return fastJSON.JSON.ToJSON(jsonObject);\n"
                      "            }}\n"
                      "\n"
                      "            public static Dictionary<string, object> ToJsonObject({0} obj)\n"
                      "            {{\n"
                      "                var jsonObject = new Dictionary<string, object>();\n").format(_capitalize(self.data.name))
        for member in self.data.data:
            if member.type == ParsedObjectType.Object:
                serializer += _serialize_object_member(member, self.namespace)
            elif member.type == ParsedObjectType.Array:
                serializer += _serialize_array_member(member, self.namespace)
            else:
                if member.type == ParsedObjectType.String:
                    serializer += "                if (obj.{0} != null)\n    ".format(_capitalize(member.name))
                serializer += "                jsonObject[\"{0}\"] = obj.{1};\n".format(member.name, _capitalize(member.name))

        serializer += ("                return jsonObject;\n"
                       "            }\n\n")
        return serializer

    def _generate_from_json(self):
        serializer = ("            public static {0} FromJson(string jsonString)\n"
                      "            {{\n"
                      "                var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);\n"
                      "                return FromJsonObject(jsonObject);\n"
                      "            }}\n"
                      "\n"
                      "            public static {0} FromJsonObject(Dictionary<string, object> jsonObject)\n"
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
    json_container_string = "jsonObject[\"{0}\"]".format(member.name)

    if member.type == ParsedObjectType.Object:
        return "                var {0} = jsonObject.ContainsKey(\"{0}\") ? {1}.{2}.FastJSONFactory.FromJsonObject({3} as Dictionary<string, object>) : null;\n".format(member.name, namespace, _capitalize(member.name), json_container_string)
    elif member.type == ParsedObjectType.Array:
        result = ("                var {2} = {1}();\n"
                  "                if(jsonObject.ContainsKey(\"{2}\"))\n"
                  "                {{\n"
                  "                    foreach({3} item in jsonObject[\"{2}\"] as List<object>)\n"
                  "                    {{\n").format(_capitalize(member.name), _get_member_initialization_string(member, json_container_string), member.name, _serialize_list_type(member.data[0]))
        child = member.data[0]

        if child.type == ParsedObjectType.Object:
            result += "                        {0}.Add({1}.{2}.FastJSONFactory.FromJsonObject(item));\n".format(member.name, namespace, _capitalize(child.name))
        else:
            result += "                        {0}.Add(item);\n".format(member.name)
        result += ("                    }\n"
                   "                }\n\n")
        return result
    elif member.type == ParsedObjectType.String:
        return "                var {0} = jsonObject.ContainsKey(\"{0}\") ? {1} as string : \"\";\n".format(member.name, _get_member_initialization_string(member, json_container_string))
    elif member.type == ParsedObjectType.Float:
        return "                var {0} = jsonObject.ContainsKey(\"{0}\") ? float.Parse({1} as string) : {3};\n".format(member.name, _get_member_initialization_string(member, json_container_string), _get_type_name(member), _get_default_value(member))
    else:
        return "                var {0} = jsonObject.ContainsKey(\"{0}\") ? ({2}){1} : {3};\n".format(member.name, _get_member_initialization_string(member, json_container_string), _get_type_name(member), _get_default_value(member))
        return result


def _get_default_value(member):
    if member.type == ParsedObjectType.Bool:
        return "false"
    if member.type == ParsedObjectType.Float:
        return "0.0f"
    if member.type == ParsedObjectType.Int:
        return "0"

    return ""


def _get_member_initialization_string(member, json_container):
    if member.type == ParsedObjectType.Object:
        return "new {0}({1})".format(_capitalize(member.name), json_container)
    if member.type == ParsedObjectType.Array:
        return "new {0}".format( _get_type_name(member))
    return json_container


def _get_type_name(member):
    """
    If a ParsedClass is supplied then it returns the object name with a captialized first letter (myClass => MyClass)
    For ParsedMember it returns the type of the member (myString => string)
    :type member: ParsedMember
    :param obj:
    :return:
    """
    if member.type == ParsedObjectType.String or member.type == ParsedObjectType.Float:
        return member.type.name.lower()
    elif member.type == ParsedObjectType.Int:
        return "long"
    elif member.type == ParsedObjectType.Bool:
        return "bool"
    elif member.type == ParsedObjectType.Array:
        return "List<{0}>".format(_get_type_name(member.data[0]))
    else:
        return _capitalize(member.name)


def _serialize_object_member(member, namespace):
    return ("                if (obj.{1} != null)\n"
            "                    jsonObject[\"{0}\"] = {2}.{1}.FastJSONFactory.ToJsonObject(obj.{1});\n").format(member.name, _capitalize(member.name), namespace)


def _serialize_array_member(member, namespace):
    serializer = ("                if(obj.{1} != null)\n"
                  "                {{\n"
                  "                    var {0} = new List<{2}>();\n").format(member.name, _capitalize(member.name), _serialize_list_type(member.data[0]))
    serializer += "                    foreach(var item in obj.{0})\n".format(_capitalize(member.name))
    serializer += "                    {\n"
    if member.data[0].type == ParsedObjectType.Object:
        serializer += "                        {0}.Add({1}.{2}.FastJSONFactory.ToJsonObject(item));\n".format(member.name, namespace, _capitalize(member.data[0].name))
    else:
        serializer += "                        {0}.Add(item);\n".format(member.name)
    serializer += "                    }\n"
    serializer += "                    jsonObject[\"{0}\"] = {0};\n".format(member.name)
    serializer += "                }\n"
    return serializer

def _capitalize(obj):
    """
    Returns the object name with the first letter capitalized (all other untouched).
    :param obj:
    :return:
    """
    if obj.__len__() < 2:
        return obj
    if obj == "string" or obj == "float" or obj == "long":
        return obj
    return obj[0].upper() + obj[1:]


def _serialize_list_type(obj):
    if obj.type == ParsedObjectType.Object:
        return "Dictionary<string,object>"
    else:
        return _get_type_name(obj)