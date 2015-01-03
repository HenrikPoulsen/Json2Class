from collections import OrderedDict
from enum import Enum


class ParsedObjectType(Enum):
    Unknown = 0
    Int = 1
    Float = 2
    String = 3
    Object = 4
    Array = 5


class ParsedObject():
    """
    Loads a json object into an object which is easier for the generators to use later.
    """
    def __init__(self, name, json):
        """

        :param name: The name of this object
        :param json:
        :return:
        """
        self.name = name
        self.data = []
        self.type = ParsedObjectType.Unknown
        self.skip = False

        print "Loading " + name
        self._load(json)
        print "Done loading " + name

    def _load(self, json):
        """
        Loads the json data at the current level of self.json and then recursively creates new ParsedObjects from the
         deeper data
        :rtype: None
        :return: None
        """
        self.type = self._load_object_type(json)

        self._load_data(json)


    def _load_object_type(self, json):
        """
        :rtype: ParsedObjectType
        :return:
        """
        t = type(json)
        if t is int:
            return ParsedObjectType.Int
        if t is float:
            return ParsedObjectType.Float
        if t is list:
            return ParsedObjectType.Array
        if t is unicode or t is str:
            return ParsedObjectType.String
        if t is OrderedDict or t is dict:
            return ParsedObjectType.Object

        raise ImportError("Unknown object type {0}".format(t))

    def _load_data(self, json):
        """
        Loads the objects nested in the current json data
        :return: None
        """
        if self.type == ParsedObjectType.Object:
            self._load_object(json)
        elif self.type == ParsedObjectType.Array:
            self._load_array(json)
        else:
            self.data = json

    def _load_array(self, json):
        for item in json:
            member = ParsedObject(self.name, item)
            self.data.append(member)
    def _load_object(self, json):
        for key in json:
            if key.startswith("@"):
                self._load_annotation(key, json[key])
                continue
            member = ParsedObject(key, json[key])
            self.data.append(member)

    def _load_annotation(self, key, value):
        if key == "@name":
            self.name = value
        elif key == "@skip_generate":
            self.skip = True
        elif key == "@namespace":
            self.namespace = value