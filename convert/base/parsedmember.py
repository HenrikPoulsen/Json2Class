from collections import OrderedDict


class ParsedMember():
    def __init__(self, name, parent):
        #print "Created member {0}".format(name)
        self.name = name
        self.type = ""
        self.parent = parent

    def load(self, json_object):
        member_type = type(json_object)

        if member_type is list:
            if json_object.__len__() > 0:
                self.type = self._member_type(member_type, type(json_object[0]))
            else:
                self.type = "[]"
        else:
            self.type = self._member_type(member_type)

    def _member_type(self, member_type, sub_type=None):
        if member_type is unicode:
            return "string"
        elif member_type is int:
            return "int"
        elif member_type is bool:
            return "bool"
        elif member_type is float:
            return "float"
        elif member_type is OrderedDict:
            return self.name
        elif member_type is list:
            return "[{0}]".format(self._member_type(sub_type))
        else:
            raise ImportError("Unknown type {0} for {1}".format(member_type, self.name))