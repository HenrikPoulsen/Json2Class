

class ParsedMember():
    def __init__(self, name):
        #print "Created member {0}".format(name)
        self.name = name
        self.type = ""


    def load(self, json_object):
        member_type = type(json_object)

        if member_type is list:
            self._set_member_type(type(json_object[0]))
        else:
            self._set_member_type(member_type)


    def _set_member_type(self, member_type):
        if member_type is unicode:
            self.type = "string"
        elif member_type is int:
            self.type = "int"
        elif member_type is bool:
            self.type = "bool"
        elif member_type is float:
            self.type = "float"
        else:
            raise ImportError("Unknown type {0} for {1}".format(member_type, self.name))