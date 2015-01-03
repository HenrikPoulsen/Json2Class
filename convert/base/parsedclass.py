from collections import OrderedDict
from convert.base.parsedmember import ParsedMember


class ParsedClass():
    def __init__(self, name):
        self.name = name
        self.members = []
        self.json = {}

    def load(self, json_object, parsed_classes):
        """
        :type json_object: dict
        :param json_object:
        :type parsed_classes: list of [ParsedClass]
        :param parsed_classes:
        :return:
        """
        self.json = json_object
        for member_name in json_object.keys():
            if member_name.startswith("@"):
                self._handle_notation(member_name, json_object[member_name], parsed_classes)
                continue

            member_type = type(json_object[member_name])

            if member_type is OrderedDict:
                new_class = ParsedClass(member_name)
                parsed_classes.append(new_class)
                new_class.load(json_object[member_name], parsed_classes)

            elif member_type is list and json_object[member_name].__len__() > 0 and type(json_object[member_name][0]) is OrderedDict:
                new_class = ParsedClass(member_name)
                parsed_classes.append(new_class)
                new_class.load(json_object[member_name][0], parsed_classes)

            self._handle_member(member_name, json_object[member_name])

    def _handle_notation(self, notation_name, notation_value, parsed_classes):
        if notation_name == "@class":
            print "Setting class name from " + self.name + " to " + notation_value + " because @class was set"
            self.name = notation_value
            # We need to set the class generated from the object this member is from to the name defined
            pass
        elif notation_name == "@namespace":
            # overrides the default namespace and makes sure the generated code imports it
            pass
        elif notation_name == "@skip_generate":
            # don't generate a class for this. Most commonly because it already exists somewhere else.
            print "Skipping class generation for " + self.name + " since @skip_generate was set"
            parsed_classes.pop()
            pass
        else:
            raise ImportError("Unknown notation" + notation_name)

    def _handle_member(self, member_name, member_json):
        new_member = ParsedMember(member_name, self)
        self.members.append(new_member)
        new_member.load(member_json)

    @classmethod
    def parse(cls, name, json_object, parsed_classes):
        """

        :type json_object: dict
        :param json_object: The object to parse
        :type parsed_classes: list of [ParsedClass]
        :param parsed_classes:
        :return:
        """

        if type(json_object) is OrderedDict:
            new_class = ParsedClass(name)
            parsed_classes.append(new_class)
            new_class.load(json_object, parsed_classes)
        else:
            raise ImportError()