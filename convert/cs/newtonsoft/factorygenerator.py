from convert.base.factorygenerator import BaseFactoryGenerator


class FactoryGenerator(BaseFactoryGenerator):
    def generate_import(self):
        return "using Newtonsoft.Json;\n"

    def generate(self, data, namespace):
        """

        :type data: ParsedObject
        :return:
        """
        self.data = data
        self.namespace = namespace
        serializers = ("\n        public static class NewtonsoftFactory\n"
                       "        {\n")
        serializers += self._generate_to_json()
        serializers += self._generate_from_json()
        serializers += "        }\n"
        return serializers

    def _generate_to_json(self):
        """serializer = ("            public static JSONNode ToJson({0} obj)\n"
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
        return serializer"""
        return ""

    def _generate_from_json(self):
        return ""

