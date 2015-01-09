import json
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-09                                                                  #
#####################################################################################


class Person:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._country = ""
        self._family = []

    @property
    def name(self):
        """:rtype: str"""
        return self._name
    @name.setter
    def name(self, value):
        """:type value: str
           :rtype: None"""
        self._name = value

    @property
    def age(self):
        """:rtype: int"""
        return self._age
    @age.setter
    def age(self, value):
        """:type value: int
           :rtype: None"""
        self._age = value

    @property
    def country(self):
        """:rtype: str"""
        return self._country
    @country.setter
    def country(self, value):
        """:type value: str
           :rtype: None"""
        self._country = value

    @property
    def family(self):
        """:rtype: list of [Person]"""
        return self._family
    @family.setter
    def family(self, value):
        """:type value: list of [Person]
           :rtype: None"""
        self._family = value



    class JsonFactory():
        @staticmethod
        def to_json(self):
            """:rtype: dict"""
            return Person.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                d = {
                    'name': obj.name,
                    'age': obj.age,
                    'country': obj.country,
                    'family': [],
                }
                for item in obj.family:
                    d['family'].append(item.to_json())

                return d

        @staticmethod
        def from_json(cls, json_obj):
            """:type json_obj: dict
               :rtype: Person"""
            obj = Person()
            obj._name = json_obj["name"]
            obj._age = json_obj["age"]
            obj._country = json_obj["country"]
            obj._family = []
            for item in json_obj["family"]:
                obj._family.append(Person.load(item))
            return obj

