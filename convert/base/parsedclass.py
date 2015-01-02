from collections import OrderedDict
from convert.base.parsedmember import ParsedMember


class ParsedClass():
    def __init__(self, name):
        self.name = name
        self.members = []

    def load(self, json_object, parsed_classes):
        """
        :type json_object: dict
        :param json_object:
        :type parsed_classes: list of [ParsedClass]
        :param parsed_classes:
        :return:
        """
        for member_name in json_object.keys():
            member_type = type(json_object[member_name])
            if member_type is OrderedDict:
                new_class = ParsedClass(member_name)
                parsed_classes.append(new_class)
                new_class.load(json_object[member_name], parsed_classes)

            elif member_type is list and json_object[member_name].__len__() > 0 and type(json_object[member_name][0]) is OrderedDict:
                new_class = ParsedClass(member_name)
                parsed_classes.append(new_class)
                new_class.load(json_object[member_name][0], parsed_classes)

            new_member = ParsedMember(member_name)
            self.members.append(new_member)
            new_member.load(json_object[member_name])

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
